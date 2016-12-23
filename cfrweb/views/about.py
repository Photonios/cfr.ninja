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
                'page': 'About',
                'description': ('CFR Ninja (cfr.ninja) is a website '
                                'that aims to provide an improved '
                                'interface when it comes to accessing '
                                'train schedules and delays in Romania.')

            }
        }
