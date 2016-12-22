import logging

import aiohttp

from cfrweb import routes


def main():
    """Entry point for this application."""

    logging.basicConfig(level=logging.DEBUG)

    app = aiohttp.web.Application()

    for methods, route, handler in routes.get():
        resource = app.router.add_resource(route)

        for method in methods:
            resource.add_route(method, handler)

    aiohttp.web.run_app(app, port=80)


if __name__ == '__main__':
    main()
