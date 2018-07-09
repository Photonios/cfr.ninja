import json

import cfr

from datetime import datetime

from .template import TemplateView


class ScheduleView(TemplateView):
    """Shows the available trains between two destinations."""

    template_name = 'templates/schedule.html'

    async def get(self):
        """Reply to HTTP GET request."""

        self.station_from = self.request.rel_url.query.get('from')
        self.station_to = self.request.rel_url.query.get('to')
        self.station_via = self.request.rel_url.query.get('via')

        return await super(ScheduleView, self).get()

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        return {
            'schedule': json.dumps(cfr.train.schedule(
                datetime.now(),
                self.station_from,
                self.station_to
            ))
        }
