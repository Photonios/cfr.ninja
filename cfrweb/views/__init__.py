from .about import AboutView
from .error import ErrorView
from .train import TrainView
from .template import TemplateView
from .find_train import FindTrainView
from .staticfile import StaticFileView

__all__ = [
    'TrainView',
    'ErrorView',
    'AboutView',
    'TemplateView',
    'FindTrainView',
    'StaticFileView',
]
