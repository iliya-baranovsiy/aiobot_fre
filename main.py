from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Bot, Dispatcher
import asyncio
from handlers.teachers import router_1
from handlers.handlers import router
from handlers.pamyatki import router_2
from handlers.kayan_test import router_3
from handlers.examens import router_4
from handlers.chem_game import router_5
from serveses.db import create_db
from load_conf import TOKEN
from serveses.message_sender import messages


async def main():
    await create_db()
    bot = Bot(token=TOKEN)
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router, router_1, router_2, router_3, router_4,router_5)
    await bot.send_message(chat_id="1832511762", text="test_ассылка")
    #try:
        #await messages(bot)
   # except:
       # pass
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())


if __name__ == "__main__":
    asyncio.run(main())
