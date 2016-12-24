from .views import AboutView, SearchView, StaticFileView, TrainView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return [
        (['GET'], '/', SearchView),
        (['GET'], '/about', AboutView),
        (['GET'], '/train/{train}', TrainView),
        (['GET'], '/train/', TrainView),
        (['GET'], '/{filename:.*}', StaticFileView)
    ]
