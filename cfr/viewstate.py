import requests
from bs4 import BeautifulSoup


class ViewState:
    """Helps in tracking __VIEWSTATE in a
    ASP.NET page using "View State".

    On these kind of pages, a "state" is kept in a
    hidden <input> named __VIEWSTATE. This is a
    base64 encoded string that contains the current
    state of a page.

    When hitting a button for example, the information
    is send to the server with the current view state
    and some other information.

    The server then replies with a new viewstate,
    based on whatever action that was requested.

    When sraping pages that work like this, we
    have to keep track of the view state and go
    through the right state changes in order for
    things to work.

    Find more:

        https://msdn.microsoft.com/en-us/library/ms972976.aspx
    """

    STATE_VARS = [
        '__VIEWSTATE',
        '__VIEWSTATEGENERATOR'
    ]

    USER_AGENT = 'cfr.ninja'

    def __init__(self, url: str):
        """Initializes a new instance of
        :see ViewState.

        Arguments:
            url:
                The URL at which the view
                state is located.
        """

        self.url = url

        self._state = dict()
        self._session = requests.Session()

    def request(self, method: str, *args, **kwargs) -> BeautifulSoup:
        """Makes a HTTP request, sending
        the current view state along and
        recording the new state.

        This is actually a proxy method
        for the :see:requests.request
        method. The URL is implied.

        Arguments:
            method:
                The HTTP method to use.

            *args:
                Additional positional
                arguments to pass to
                the requests library.

            **kwargs:
                Additional keyword
                arguments to pass to
                the requests library.

        Returns:
            The response from the server.
        """

        # only create a new dict if the user
        # didn't specify any at all
        kwargs['data'] = kwargs.get('data', dict())

        # specify the current state as form vars
        kwargs['data'].update(self._state)

        # override the user agent
        kwargs['headers'] = kwargs.get('headers', dict())
        kwargs['headers'].update({
            'User-agent': self.USER_AGENT
        })

        # make the http request
        response = self._session.request(
            method,
            self.url,
            *args,
            **kwargs
        )

        assert response.status_code == 200

        # parse the response and extract the state
        document = BeautifulSoup(response.text, 'html.parser')
        self._extract_state(document)

        return document

    def _extract_state(self, document: BeautifulSoup) -> None:
        """Extracts the current state from the
        specified document.

        Arguments:
            document:
                The HTML document to extract
                the state from.
        """

        self._state = {
            state_var: document.find(id=state_var).get('value')
            for state_var in self.STATE_VARS
        }
