from aiohttp import web

from .. import template


class TemplateView(web.View):
    """Allows rendering a Jinja2 template."""

    async def get(self):
        """Reply to HTTP GET request."""

        template_name = getattr(
            self,
            'template_name'
        )

        rendered_template = template.render(
            template_name,
            self.context(),
            self.request.language
        )

        return web.Response(
            content_type='text/html',
            text=rendered_template
        )

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return dict()
