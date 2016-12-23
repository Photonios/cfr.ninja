from .template import TemplateView


class HomeView(TemplateView):
    """Page that is displayed when you open the website."""

    template_name = 'templates/index.html'

    def context(self):
        """Gets the context for the template."""

        return {
            'meta': {
                'description': 'Real-time updates on trains in Romania.'
            }
        }
