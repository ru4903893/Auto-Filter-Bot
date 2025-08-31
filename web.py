web_app.py
from aiohttp import web

# হেলথ চেক (যাতে Render / Koyeb দেখে যে বট চালু আছে)
async def handle(request):
    return web.Response(text="Bot is Alive!")

# অ্যাপ তৈরি
web_app = web.Application()
web_app.router.add_get("/", handle)
