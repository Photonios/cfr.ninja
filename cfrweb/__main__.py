import logging
import argparse

import aiohttp
import aiohttp.web
import aiohttp_cache

from . import middleware
from .urls import urlconfig
from .config import settings


def _parse_arguments() -> argparse.Namespace:
    """Parses the command line arguments."""

    parser = argparse.ArgumentParser(description='cfr.ninja web server')

    parser.add_argument('--port',
                        default=8080,
                        type=int,
                        help='Port to listen on.')

    return parser.parse_args()


def _enable_caching(app: aiohttp.web.Application):
    """Enables Redis-based caching for the
    specified aiohttp application.

    Arguments:
        app:
            The application to cache for.
    """

    aiohttp_cache.setup_cache(
        app,
        cache_type='redis',
        backend_config=aiohttp_cache.RedisConfig(
            host=settings.REDIS_URL.hostname,
            port=settings.REDIS_URL.port,
            password=settings.REDIS_URL.password,
            key_prefix='cfrninja'
        )
    )


def main():
    """Entry point for this application."""

    logging.basicConfig(level=logging.DEBUG)

    app = aiohttp.web.Application(
        middlewares=[
            middleware.locale,
            middleware.security,
            middleware.browser_cache,
            middleware.exception
        ],
        router=urlconfig.dispatcher
    )

    arguments = _parse_arguments()

    if not settings.DEBUG:
        _enable_caching(app)

    aiohttp.web.run_app(app, port=arguments.port)


if __name__ == '__main__':
    main()
