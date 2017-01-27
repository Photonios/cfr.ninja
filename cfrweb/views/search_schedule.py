from .template import TemplateView


class SearchScheduleView(TemplateView):
    """Page that allows searching for trains based on the
    destination and the time of leaving."""

    template_name = 'templates/search_schedule.html'
