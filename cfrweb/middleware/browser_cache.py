from ..config import settings

async def browser_cache(_, handler):
    """Browser cache middleware for aiohttp,
    which adds the 'Cache-control' headers
    to each response.

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

        if settings.DEBUG:
            value = 'no-cache'
        else:
            value = 'max-age=%d' % settings.CACHE_TIMEOUT

        response.headers['Cache-Control'] = value

        return response

    return middleware_handler
