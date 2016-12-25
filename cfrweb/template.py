import jinja2

from . import i18n, filters
from .util import merge_dict_r
from .config import settings


def render(name: str, context: dict, language: str=None) -> str:
    """Renders the template at the specified path
    with the specified context.

    Arguments:
        name:
            The name/path to the template to render.

        context:
            The context to provide to the template.

        language:
            Optionally, the language to render in.

    Returns:
        The rendered template.
    """

    loader = loader = jinja2.FileSystemLoader(
        settings.PROJECT_DIR
    )

    environment = jinja2.Environment(
        loader=loader,
        extensions=['jinja2.ext.i18n']
    )

    # register all the filters we have
    environment.filters['local_url'] = filters.local_url

    # install the current locale so that gettext
    # works properly
    locale = i18n.get(language)
    environment.install_gettext_translations(locale)

    # build the complete context by combining
    # the defaults with the ones specified to us
    complete_context = merge_dict_r(
        settings.TEMPLATES_DEFAULT_CONTEXT,
        merge_dict_r(
            context,
            {'meta': {'language': language}}
        )
    )

    # render the template
    template = environment.get_template(name)
    rendered_template = template.render(complete_context)

    return rendered_template
