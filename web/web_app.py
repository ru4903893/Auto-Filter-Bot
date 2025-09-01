from aiohttp import web

# হেলথ চেক
async def handle(request):
    return web.Response(text="Bot is Alive!")

# অ্যাপ তৈরি
web_app = web.Application()
web_app.router.add_get("/", handle)
