from .views import AboutView, TrainView, SearchView, StaticFileView
from .routing import Url, UrlCollection

urlconfig = UrlCollection([
    Url(
        url='/',
        name='home',
        view=SearchView
    ),
    Url(
        url='/',
        name='train_search',
        view=SearchView
    ),
    Url(
        url='/about',
        name='about',
        view=AboutView
    ),
    Url(
        url='/train/{train}',
        name='train_specific',
        view=TrainView
    ),
    Url(
        url='/train',
        name='train_dynamic',
        view=TrainView
    ),
    Url(
        url='/{filename:.*}',
        name='staticfile',
        view=StaticFileView
    )
])
