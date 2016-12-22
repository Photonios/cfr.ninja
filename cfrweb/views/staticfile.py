import mimetypes
import os

from aiohttp import web

from ..config import settings


class StaticFileView(web.View):
    """Allows loading an arbitrary file from disk."""

    async def get(self):
        """Reply to HTTP GET request."""

        filename = self.request.match_info.get('filename')
        filepath = os.path.join(
            settings.STATIC_FILES_DIR,
            filename
        )

        try:
            with open(filepath, 'rb') as file:
                filecontents = file.read()
        except FileNotFoundError:
            return web.Response(
                status=404,
                text='404 Not Found'
            )

        return web.Response(
            content_type=mimetypes.guess_type(filename)[0],
            body=filecontents
        )
