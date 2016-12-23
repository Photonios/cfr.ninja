from .template import TemplateView


class HomeView(TemplateView):
    """Page that is displayed when you open the website."""

    template_name = 'templates/index.html'
