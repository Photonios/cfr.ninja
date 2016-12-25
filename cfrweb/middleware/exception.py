from aiohttp import web

from ..views import ErrorView

async def exception(_, handler):
    """Catches exceptions and provides
    the right error template with
    the message contained in the exception.

    Arguments:
        _:
            Unused argument.

        handler:
            The next handler to invoke.

    Returns:
        The middleware handler.
    """

    async def middleware_handler(request):
        try:
            return await handler(request)
        except web.HTTPError as error:
            request.match_info['message'] = error.reason
            return await ErrorView(request).get()

    return middleware_handler
