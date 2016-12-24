from .template import TemplateView


class SearchView(TemplateView):
    """Page that allows searching trains by number."""

    template_name = 'templates/search.html'
