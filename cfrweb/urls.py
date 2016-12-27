from .views import (AboutView, TrainView, SearchView, FindTrainView,
                    StaticFileView)
from .routing import Url, UrlCollection

urlconfig = UrlCollection([
    Url(
        url='/',
        name='home',
        view=FindTrainView
    ),
    Url(
        url='/search',
        name='search',
        view=SearchView
    ),
    Url(
        url='/',
        name='find_train',
        view=FindTrainView
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
