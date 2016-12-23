from .template import TemplateView


class HomeView(TemplateView):
    """Page that is displayed when you open the website."""

    template_name = 'templates/index.html'

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return dict()
