from .. import i18n

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
        request.locale = i18n.get('en')
        response = await handler(request)
        return response

    return middleware_handler
