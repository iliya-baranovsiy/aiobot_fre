from aiogram import F, Router, types
from serveses.keybords import *
from serveses.texts import *
import time

router_1 = Router()


@router_1.callback_query(F.data == "teachers")
async def ans_1(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb_2)
    await call.message.edit_text("Выберете преподавателя", reply_markup=buttons)


@router_1.callback_query(F.data == "MAs")
async def math(call: CallbackQuery):
    await call.message.answer_photo(caption=text_math, photo=types.FSInputFile("datas/template_1/kayan.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_1.callback_query(F.data == "chemistrys")
async def math(call: CallbackQuery):
    await call.message.answer_photo(caption=text_chem, photo=types.FSInputFile("datas/template_1/chem.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_1.callback_query(F.data == "ebriys")
async def math(call: CallbackQuery):
    await call.message.answer_photo(caption=text_ebriy, photo=types.FSInputFile("datas/template_1/ebr.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_1.callback_query(F.data == "omvpps")
async def math(call: CallbackQuery):
    await call.message.answer_photo(caption=text_omvpp, photo=types.FSInputFile("datas/template_1/omvpp.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_1.callback_query(F.data == "oaips")
async def math(call: CallbackQuery):
    await call.message.answer_photo(caption=text_oaip, photo=types.FSInputFile("datas/template_1/oaip.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)
