import json
import datetime

import cfr

from .template import TemplateView


class ScheduleView(TemplateView):
    """Shows the available trains between two destinations."""

    template_name = 'templates/schedule.html'

    async def get(self):
        """Reply to HTTP GET request."""

        self.station_from = self.request.match_info.get('from')
        self.station_to = self.request.match_info.get('to')
        self.station_via = self.request.match_info.get('via')

        return await super(ScheduleView, self).get()

    def context(self) -> dict:
        """Gets the context to render the
        template with.

        Returns:
            The context to pass to the template.
        """

        self.station_from = self.request.GET.get('from')
        self.station_to = self.request.GET.get('to')
        self.station_via = self.request.GET.get('via')

        return {
            'schedule': json.dumps(cfr.train.schedule(
                datetime.date(2017, 1, 27),
                self.station_from,
                self.station_to
            ))
        }
