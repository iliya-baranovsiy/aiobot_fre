from serveses.db import select
from serveses.texts import pre_relis
from aiogram import types
from aiogram.types import InputMediaPhoto


async def messages(bot):
    users_id = await select()
    flag = True
    photos = [
        InputMediaPhoto(media=types.FSInputFile("datas/pre/pres.png"),caption=pre_relis),
        InputMediaPhoto(media=types.FSInputFile("datas/pre/eppre.png")),
        InputMediaPhoto(media=types.FSInputFile("datas/pre/apre.png"))
    ]
    while flag == True:
        for i in users_id:
            try:
                await bot.send_media_group(chat_id=i, media=photos)
            except:
                pass
        flag = False
