from cfrweb.config import settings
import jinja2


def merge_dict_r(dict_a: dict, dict_b: dict):
    for key, value in dict_b.items():
        if isinstance(dict_a.get(key), dict):
            merge_dict_r(dict_a[key], value)
        else:
            dict_a[key] = value


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

    complete_context = settings.TEMPLATES_DEFAULT_CONTEXT.copy()
    merge_dict_r(complete_context, context)

    rendered_template = template.render(complete_context)
    return rendered_template
