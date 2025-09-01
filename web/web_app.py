from aiohttp import web

# --- বট চালু আছে কিনা চেক করার জন্য একটি হ্যান্ডলার ---
async def handle(request):
    return web.Response(text="✅ Bot is Alive and Running!")

# --- Web App তৈরি করা ---
def create_app():
    app = web.Application()
    app.router.add_get("/", handle)  # মূল রুটে ("/") Alive মেসেজ দেখাবে
    return app

# --- সার্ভার চালু করার এন্ট্রি পয়েন্ট ---
if __name__ == "__main__":
    web.run_app(create_app(), host="0.0.0.0", port=8080)
