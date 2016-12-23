from .template import TemplateView


class AboutView(TemplateView):
    """Page that describes this website."""

    template_name = 'templates/about.html'

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return {
            'meta': {
                'page': 'About'
            }
        }
