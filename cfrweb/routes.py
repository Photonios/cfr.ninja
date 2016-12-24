import collections

from .views import AboutView, TrainView, SearchView, StaticFileView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return collections.OrderedDict([
        ('/', SearchView),
        ('/about', AboutView),
        ('/train/{train}', TrainView),
        ('/train/', TrainView),
        ('/{filename:.*}', StaticFileView)
    ])
