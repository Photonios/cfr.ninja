from .views import (
    AboutView,
    TrainView,
    ScheduleView,
    FindTrainView,
    StaticFileView,
    SearchScheduleView
)

from .routing import Url, UrlCollection

urlconfig = UrlCollection([
    Url(
        url='/',
        name='home',
        view=FindTrainView
    ),
    Url(
        url='/schedule',
        name='search_schedule_result',
        view=ScheduleView
    ),
    Url(
        url='/search-schedule',
        name='search_schedule',
        view=SearchScheduleView
    ),
    Url(
        url='/find-train',
        name='find_train',
        view=FindTrainView
    ),
    Url(
        url='/train/{train}',
        name='find_train_result',
        view=TrainView
    ),
    Url(
        url='/train',
        name='find_train_result_dynamic',
        view=TrainView
    ),
    Url(
        url='/about',
        name='about',
        view=AboutView
    ),
    Url(
        url='/{filename:.*}',
        name='staticfile',
        view=StaticFileView
    )
])
