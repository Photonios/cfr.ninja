from .views import AboutView, HomeView, StaticFileView, TrainView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return [
        (['GET'], '/', HomeView),
        (['GET'], '/about', AboutView),
        (['GET'], '/train/{train}', TrainView),
        (['GET'], '/train/', TrainView),
        (['GET'], '/{filename:.*}', StaticFileView)
    ]
