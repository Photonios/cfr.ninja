from aiohttp import web
from aiohttp_cache import cache
import cfr

from .template import TemplateView


@cache(expires=60)
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
                '/%s/train/%s' % (self.request.language, self.train_number)
            )

        self.train_number = self.request.match_info.get('train')
        return await super(TrainView, self).get()

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        try:
            context = cfr.train.find(self.train_number)

            meta_description = ('Real-time updates for {rank}'
                                '{number}, on the route \'{route}\'.'
                                ).format(**context)

            context.update({
                'meta': {
                    'page': '%s%s' % (context['rank'], context['number']),
                    'description': meta_description
                }
            })

            return context
        except cfr.train.TrainNotFound:
            raise web.HTTPNotFound(reason='We couldn\'t find that train')
