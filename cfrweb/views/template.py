from aiohttp import web
import jinja2

from cfrweb.config import settings


class TemplateView(web.View):
    """Allows rendering a Jinja2 template."""

    async def get(self):
        template_name = getattr(
            self,
            'template_name'
        )

        loader = loader = jinja2.FileSystemLoader(
            settings.PROJECT_DIR
        )

        environment = jinja2.Environment(loader=loader)
        template = environment.get_template(template_name)

        rendered_template = template.render(self._get_context())

        return web.Response(
            content_type='text/html',
            text=rendered_template
        )

    def _get_context(self):
        """Gets the context to pass to the
        Jinja2 template from the super class."""

        context = getattr(
            self,
            'context',
            lambda: dict()
        )

        return context()
