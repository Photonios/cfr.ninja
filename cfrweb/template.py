from cfrweb.config import settings
import jinja2


def render(name: str, context: dict) -> str:
    """Renders the template at the specified path
    with the specified context.

    Arguments:
        name:
            The name/path to the template to render.

        context:
            The context to provide to the template.

    Returns:
        The rendered template.
    """

    loader = loader = jinja2.FileSystemLoader(
        settings.PROJECT_DIR
    )

    environment = jinja2.Environment(loader=loader)
    template = environment.get_template(name)

    complete_context = settings.TEMPLATES_DEFAULT_CONTEXT
    complete_context.update(context)

    rendered_template = template.render(complete_context)
    return rendered_template
