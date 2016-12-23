import argparse
import logging

from cfrweb import middleware, routes
import aiohttp


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
        middlewares=[middleware.browser_cache]
    )

    arguments = _parse_arguments()

    for methods, route, handler in routes.get():
        resource = app.router.add_resource(route)

        for method in methods:
            resource.add_route(method, handler)

    aiohttp.web.run_app(app, port=arguments.port)


if __name__ == '__main__':
    main()
