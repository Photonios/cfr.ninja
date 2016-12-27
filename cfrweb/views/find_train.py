from .template import TemplateView


class FindTrainView(TemplateView):
    """Page that allows searching trains by number."""

    template_name = 'templates/find_train.html'
