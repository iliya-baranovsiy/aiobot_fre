import time
from aiogram import F, Router, types
from serveses.keybords import *
from aiogram.types import InputMediaPhoto

router_4 = Router()


@router_4.callback_query(F.data == "exes")
async def ans_1(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb_exes)
    await call.message.edit_text("Выберете предмет", reply_markup=buttons)


@router_4.callback_query(F.data == "history")
async def history(call: CallbackQuery):
    photos = [InputMediaPhoto(media=types.FSInputFile("datas/photo_exes/photo_5350701121448042426_1.jpg"),
                              caption="Вопросы к ИстБг 📔"),
              InputMediaPhoto(media=types.FSInputFile("datas/photo_exes/photo_5350701121448042428_2.jpg")),
              InputMediaPhoto(media=types.FSInputFile("datas/photo_exes/photo_5350701121448042431_3.jpg"))]
    await call.message.answer_media_group(photos)
    time.sleep(3)
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_4.callback_query(F.data == "chem_ex")
async def chem(call: CallbackQuery):
    await call.message.answer_document(caption="Вопросы по Химии 💊", document=types.FSInputFile(
        "datas/photo_exes/Вопросы к экзамену_2024_ФКП, ФРЭ (1).pdf"))
    time.sleep(3)
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)
