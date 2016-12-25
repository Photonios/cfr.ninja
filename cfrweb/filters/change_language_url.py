import jinja2


@jinja2.contextfunction
def change_language_url(context, language: str):
    """Gets the URL to change the language of
    the current page.

    Arguments:
        language:
            The language to switch to.

    Returns:
        A URL that leads to the current
        page in the specified language.
    """

    return '/%s%s' % (language, context['meta']['path'])
