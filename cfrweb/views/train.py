from aiohttp import web

from .template import TemplateView
import cfr


class TrainView(TemplateView):
    """Page that displays details about a specific train."""

    template_name = 'train.html'

    async def get(self):
        """Reply to HTTP GET request."""

        self.train_number = self.request.GET.get('train', None)
        if not self.train_number:
            return web.Response(
                status=404,
                text='404 Not Found'
            )

        return await super(TrainView, self).get()

    def context(self):
        """Gets the context for the template."""

        return cfr.train.find(self.train_number)
