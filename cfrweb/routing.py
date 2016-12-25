from typing import List

from aiohttp.web_urldispatcher import UrlDispatcher


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

    def get_url(self, name, language=None, **kwargs):
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
