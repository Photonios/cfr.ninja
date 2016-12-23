from ..config import settings

async def security(_, handler):
    """Middleware that hides potentially
    interesting information from our
    responses.

    This includes for example the 'Server'
    header, which might leak our server
    configuration to a potential attacker.

    Arguments:
        _:
            Unused argument.

        handler:
            The next handler to invoke.

    Returns:
        The middleware handler.
    """

    async def middleware_handler(request):
        response = await handler(request)

        # don't leak our server information
        response.headers['Server'] = ''

        return response

    return middleware_handler
