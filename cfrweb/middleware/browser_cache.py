import fnmatch

from ..config import settings

async def browser_cache(_, handler):
    """Browser cache middleware for aiohttp,
    which adds the 'Cache-control' headers
    to each response.

    When the application is in debug
    mode, then 'no-cache' is used, while
    if in production, then the value
    of the CACHE_TIMEOUT setting is used.

    Arguments:
        _:
            Unused argument.

        handler:
            The next handler to invoke.

    Returns:
        The middleware handler.
    """

    def _get_timeout(content_type: str):
        """Gets the cache timeout in
        seconds for a resource of the
        specified content type.

        Arguments:
            content_type:
                The content type
                to get the cache
                timeout for.

        Returns:
            The cache timeout for
            a resource of the specified
            content type.
        """

        for pattern, timeout in settings.CACHE_TIMEOUT.items():
            if fnmatch.fnmatch(content_type, pattern):
                return timeout

        return settings.CACHE_TIMEOUT['*']

    async def middleware_handler(request):
        response = await handler(request)

        if settings.DEBUG:
            value = 'no-cache'
        else:
            value = 'max-age=%d' % _get_timeout(response.content_type)

        response.headers['Cache-Control'] = value

        return response

    return middleware_handler
