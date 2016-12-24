from aiohttp import web

from .. import template

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
            response = await handler(request)
        except web.HTTPError as error:
            error.content_type = 'text/html'
            error.text = template.render(
                'templates/error.html',
                {
                    'message': error.reason
                }
            )

            return error

        return response

    return middleware_handler
