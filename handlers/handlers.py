import time
from aiogram import types, F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from serveses.keybords import *
from serveses.roffles import random_roffles
from serveses.texts import *
from serveses.db import create_record

router = Router()


@router.message(CommandStart())
async def start_message(msg: Message):
    id = msg.chat.id
    # 1832511762
    f_name = msg.chat.first_name
    last_name = msg.chat.last_name
    await create_record(id, f_name, last_name)
    buttons = InlineKeyboardMarkup(inline_keyboard=kb)
    await msg.answer_photo(caption=text_1, photo=types.FSInputFile("datas/template_1/photo_1.jpg"))
    await msg.answer("Выберете то, что хотите посмотреть", reply_markup=buttons)


@router.callback_query(F.data == "roffles")
async def ans_1(call: CallbackQuery):
    try:
        photo = random_roffles()
        await call.message.answer_photo(photo=types.FSInputFile(photo))
        buttons = InlineKeyboardMarkup(inline_keyboard=kb)
        time.sleep(2)
        await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)
    except:
        video = random_roffles()
        await call.message.answer_video(video=types.FSInputFile(video))
        buttons = InlineKeyboardMarkup(inline_keyboard=kb)
        time.sleep(2)
        await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router.callback_query(F.data == "kayn")
async def ans_1(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    await call.message.answer(text_2)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router.callback_query(F.data == "back_1")
async def back(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb)
    await call.message.edit_text("Для продолжения выберете одну из функций", reply_markup=buttons)


@router.callback_query(F.data == "menu")
async def back_1(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb)
    await call.message.edit_text("Для продолжения выберете одну из функций", reply_markup=buttons)
