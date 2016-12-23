from .views import HomeView, StaticFileView, TrainView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return [
        (['GET'], '/', HomeView),
        (['GET'], '/train/{train}', TrainView),
        (['GET'], '/train/', TrainView),
        (['GET'], '/{filename:.*}', StaticFileView)
    ]
