import logging
import argparse

import aiohttp
import aiohttp.web

from . import middleware
from .urls import urlconfig
from .routing import LocalizedApplication


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

    app = LocalizedApplication(
        middlewares=[
            middleware.security,
            middleware.browser_cache,
            middleware.exception
        ],
        router=urlconfig.dispatcher
    )

    arguments = _parse_arguments()

    aiohttp.web.run_app(app, port=arguments.port)


if __name__ == '__main__':
    main()
