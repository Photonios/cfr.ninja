from .views import HomeView
from .views import StaticFileView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return [
        (['GET'], '/', HomeView),
        (['GET'], '/{filename}', StaticFileView)
    ]
