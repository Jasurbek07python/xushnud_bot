import  asyncio
from aiogram import Bot,Dispatcher
from dotenv import load_dotenv
import  os
import funksyalar
from aiogram.filters import  Command
from aiogram.types import  Message
from aiogram.client.session.aiohttp import AiohttpSession
load_dotenv(override=True)
dp=Dispatcher()
@dp.startup()
async def bot_ishlaganda(bot:Bot):
    await  bot.send_message(chat_id=os.getenv("Admin_id"),text="Bot ishladi.🔊")
@dp.shutdown()
async def bot_tohtaganda(bot:Bot):
    await  bot.send_message(chat_id=os.getenv("Admin_id"),text="Bot tohtadi 🔈")
@dp.message(Command("start"))
async def start_bosilganda(m:Message):
    await m.answer(f"hush kelibsiz {m.from_user.full_name}")
@dp.message(Command("help"))
async def help_bosilganda(m:Message):
    await m.answer(f"yordam bolimi hurmatli: {m.from_user.full_name}")
@dp.message()
async def echo(m:Message):
    try:
        await  m.answer(funksyalar.obhavo(funksyalar.lakatsyani_aniqlash(m.text)))
    except:
        await  m.answer("shahar nomini togri kiriting")

async def main():
    session=AiohttpSession(proxy="http://proxy.server:3128/")
    bot=Bot(token=os.getenv("bot_token"),session=session)
    await dp.start_polling(bot)
if __name__=='__main__':
    asyncio.run(main())
