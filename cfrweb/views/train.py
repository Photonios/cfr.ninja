
from aiohttp import web
import cfr

from .template import TemplateView


class TrainView(TemplateView):
    """Page that displays details about a specific train."""

    template_name = 'templates/train.html'

    async def get(self):
        """Reply to HTTP GET request."""

        # if the train number is specified through
        # a GET parameter, redirect to the perma link
        self.train_number = self.request.GET.get('train', None)
        if self.train_number:
            return web.HTTPMovedPermanently(
                '/train/%s' % self.train_number
            )

        self.train_number = self.request.match_info.get('train')
        return await super(TrainView, self).get()

    def context(self) -> dict:
        """Gets the context for the template."""

        try:
            context = cfr.train.find(self.train_number)
            context.update({
                'meta': {
                    'description': 'Real-time updates on {rank}{number}, on route \'{route}\'.'.format(**context)
                }
            })

            return context
        except cfr.train.TrainNotFound:
            raise web.HTTPNotFound(reason='We couldn\'t find that train.')
