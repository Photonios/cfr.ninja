from .template import TemplateView


class AboutView(TemplateView):
    """Page that describes this website."""

    template_name = 'templates/about.html'
