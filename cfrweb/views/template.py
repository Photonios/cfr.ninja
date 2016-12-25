from aiohttp import web
import jinja2

from .. import i18n, filters
from ..util import merge_dict_r
from ..config import settings


class TemplateView(web.View):
    """Allows rendering a Jinja2 template."""

    async def get(self):
        """Reply to HTTP GET request."""

        template_name = getattr(
            self,
            'template_name'
        )

        environment = jinja2.Environment(
            loader=jinja2.FileSystemLoader(
                settings.PROJECT_DIR
            ),
            extensions=['jinja2.ext.i18n']
        )

        # register all the filters and context functions we have
        environment.globals['url'] = filters.url
        environment.globals['change_language_url'] = filters.change_language_url

        # install the current locale so that gettext
        # works properly
        locale = i18n.get(self.request.language)
        environment.install_gettext_translations(locale)

        # build the complete context by combining
        # the defaults with the ones specified to us
        complete_context = merge_dict_r(
            settings.TEMPLATES_DEFAULT_CONTEXT,
            merge_dict_r(
                self.context(),
                {'meta': {
                    'language': self.request.language,
                    'path': self.request.path
                }}
            )
        )

        # render the template
        template = environment.get_template(template_name)
        rendered_template = template.render(complete_context)

        return web.Response(
            content_type='text/html',
            text=rendered_template
        )

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return dict()
