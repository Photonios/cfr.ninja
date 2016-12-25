from .template import TemplateView


class ErrorView(TemplateView):
    """Page that is displayed when an error occurs."""

    template_name = 'templates/error.html'

    def context(self):
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return {
            'message': self.request.match_info.get('message')
        }
