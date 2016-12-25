import jinja2


@jinja2.contextfunction
def url(context, name: str, language: str=None, **kwargs) -> str:
    """Gets the URL for the for the URL configuration with
    the specified name.

    Arguments:
        name:
            The name of the configured URL.

        language:
            The language to get the URL in.
            If none is specified, the resulting
            URL will be in whatever the current
            language is.

        **kwargs:
            Keyword arguments to pass
            to the configured URL.

    Returns:
        A URL leading to the configured URL
        with the speicfied name.
    """

    from ..urls import urlconfig

    language = language or context['meta']['language']
    return urlconfig.get_url(name, language, **kwargs)
