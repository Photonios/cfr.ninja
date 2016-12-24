import jinja2

from .util import merge_dict_r
from .config import settings


def render(name: str, context: dict, locale=None) -> str:
    """Renders the template at the specified path
    with the specified context.

    Arguments:
        name:
            The name/path to the template to render.

        context:
            The context to provide to the template.

        locale:
            Optionally, the locale to render with.

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

    environment.install_gettext_translations(locale)

    template = environment.get_template(name)

    complete_context = merge_dict_r(
        settings.TEMPLATES_DEFAULT_CONTEXT,
        context
    )

    rendered_template = template.render(complete_context)
    return rendered_template
