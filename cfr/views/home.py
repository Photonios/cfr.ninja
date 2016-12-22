from aiohttp import web


class HomeView(web.View):
    """Page that is displayed when you open the website."""

    async def get(self):
        return web.Response(text='Always be yourself. Unless you can be Batman. Then be Batman!')
