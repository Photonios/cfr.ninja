from .. import i18n
from ..config import settings

async def locale(_, handler):
    """Middleware that determines the user's
    preferred lanaguage based on the headers
    received by the server.

    The preferred language is then passed
    on to the request handler through the
    request object.

    Arguments:
        _:
            Unused argument.

        handler:
            The next handler to invoke.

    Returns:
        The middleware handler.
    """

    async def middleware_handler(request):
        # extract the language from the url
        language = request.path.split('/')[1]
        if language not in settings.I18N_LANGUAGES:
            language = settings.I18N_PRIMARY_LANGUAGE

        # build a new url without the language in it
        url = str(request.rel_url).replace('/%s' % language, '')

        # build a new request object with the new url
        new_request = request.clone(rel_url=url)
        new_request.locale = i18n.get(language)
        new_request._match_info = request._match_info

        # resolve the newly constructed url and update
        # the match information, this will make sure that
        # the right handler is invoked at the end of the road
        new_request._match_info = await new_request.app.router.resolve(new_request)

        # invoke the next handler in the tree
        response = await handler(new_request)
        return response

    return middleware_handler
