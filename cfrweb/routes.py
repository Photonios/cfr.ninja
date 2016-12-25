from .views import AboutView, TrainView, SearchView, StaticFileView


def get():
    """Gets the available HTTP routes on
    this webserver."""

    return [
        ('/', 'search', SearchView),
        ('/about', 'about', AboutView),
        ('/train/{train}', 'train', TrainView),
        ('/train/', None, TrainView),
        ('/{filename:.*}', 'staticfile', StaticFileView)
    ]
