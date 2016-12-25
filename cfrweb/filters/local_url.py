import jinja2


@jinja2.contextfilter
def local_url(context, url) -> str:
    """Displays a local url, but takes care to include
    the current language in the resulting URL.

    This means that when the specified URL is /about
    and the current language is 'ro', the resulting
    URL will be: /ro/about.

    Arguments:
        context:
            The Jinja2 template context.

        url:
            The URL to display.

    Returns:
        A local URL that may or may not
        contain a language prefix.
    """

    language = context['meta']['language']
    return '/%s%s' % (language, url)
