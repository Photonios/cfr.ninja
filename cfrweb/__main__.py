import argparse
import logging

import aiohttp
import aiohttp.web
import aiohttp_cache

from . import middleware, routes
from .config import settings


def _parse_arguments() -> argparse.Namespace:
    """Parses the command line arguments."""

    parser = argparse.ArgumentParser(description='cfr.ninja web server')

    parser.add_argument('--port',
                        default=8080,
                        type=int,
                        help='Port to listen on.')

    return parser.parse_args()


def main():
    """Entry point for this application."""

    logging.basicConfig(level=logging.DEBUG)

    app = aiohttp.web.Application(
        middlewares=[
            middleware.security,
            middleware.browser_cache,
            middleware.exception
        ]
    )

    aiohttp_cache.RedisConfig(
        host=settings.REDIS_URL.hostname,
        port=settings.REDIS_URL.port,
        password=settings.REDIS_URL.password,
        key_prefix='cfrninja'
    )

    aiohttp_cache.setup_cache(
        app,
        cache_type='redis'
    )

    arguments = _parse_arguments()

    for methods, route, handler in routes.get():
        resource = app.router.add_resource(route)

        for method in methods:
            resource.add_route(method, handler)

    aiohttp.web.run_app(app, port=arguments.port)


if __name__ == '__main__':
    main()
