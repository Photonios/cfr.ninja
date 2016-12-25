from typing import List

from aiohttp.web_urldispatcher import UrlDispatcher
import aiohttp
import aiohttp.web

from . import i18n
from .config import settings


class Url:
    """A dynamic url that requests can be routed to."""

    def __init__(self, **kwargs):
        """Initializes a new instance of :see:Url."""

        self._url = kwargs.get('url')
        self._name = kwargs.get('name', None)
        self._view = kwargs.get('view')

    @property
    def url(self):
        """Gets the URL for this route."""

        return self._url

    @property
    def name(self):
        """Gets the name of this route."""

        return self._name

    @property
    def view(self):
        """Gets the view that gets invoked upon
        this route."""

        return self._view


class UrlCollection:
    """Collection or route-able URLs."""

    def __init__(self, urls: List[Url]):
        """Initializes a new instance of :see:UrlCollection.

        Arguments:
            urls:
                A list of URLS to initialize
                the router with.
        """

        self._urls = urls
        self._dispatcher = self._make_dispatcher()

    def get_view(self, name: str):
        """Gets the view associated with the configured
        URL of the specified name.

        Arguments:
            name:
                The name of the configured URL
                to get the view of.

        Returns:
            The view associated with the configured
            URL of the specified name.
        """

        return self.dispatcher[name]

    def get_url(self, name: str, language: str=None, **kwargs):
        """Builds a valid URL to the configured
        URL with the specified name.

        Arguments:
            name:
                The name of the URL.

            **kwargs:
                Keyword arguments
                to pass to the view.

        Returns:
            A URL that leads to the configured
            URL with the specified name.
        """

        language = language or settings.I18N_PRIMARY_LANGUAGE
        url = self.dispatcher[name].url_for(**kwargs)

        return '/%s%s' % (language, url)

    @property
    def dispatcher(self) -> UrlDispatcher:
        """Gets the aiohttp :see:UrlDispatcher
        for this collection of urls."""

        return self._dispatcher

    def _make_dispatcher(self) -> UrlDispatcher:
        """Creates a aiohttp :see:UrlDispatcher based on
        the configured list of urls.

        Returns:
            A aiohttp :see:UrlDispatcher containing
            the configured urls.
        """

        dispatcher = UrlDispatcher()
        dispatcher.post_init(self)

        for url in self._urls:
            resource = dispatcher.add_resource(
                url.url,
                name=url.name
            )

            resource.add_route('GET', url.view)

        return dispatcher


class LocalizedApplication(aiohttp.web.Application):
    """Special version of the :see:aiohttp application
    that overrides the handler and takes care of extracting
    the preferred language from the URL.

    This applies to URLs such as:

        /ro/about
        /en/about
    """

    async def _handle(self, request):
        """Routes the specified request to
        the right handler:

        Arguments:
            request:
                The request to route.
        """

        language = request.path.split('/')[1]
        if language not in settings.I18N_LANGUAGES:
            language = settings.I18N_PRIMARY_LANGUAGE

        # build a new url without the language in it
        url = str(request.rel_url).replace('/%s' % language, '')

        # build a new request object with the new url
        new_request = request.clone(rel_url=url)
        new_request.locale = i18n.get(language)
        new_request.language = language

        return await super()._handle(new_request)
