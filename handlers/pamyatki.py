from aiogram import F, Router, types
from serveses.keybords import *
from aiogram.types.input_file import FSInputFile
import time

router_2 = Router()


@router_2.callback_query(F.data == "subjects")
async def ans_1(call: CallbackQuery):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb_1)
    await call.message.edit_text("Выберете предмет", reply_markup=buttons)


@router_2.callback_query(F.data == "MA")
async def ans_1(call: CallbackQuery):
    await call.message.answer_document(caption="Памятка по МА 🤓", document=FSInputFile(
        "datas/pamyatki/[Maikov_E.V.]_Vvedenie_v_matematichesky_analiz(BookSee.org).pdf"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_2.callback_query(F.data == "laiag")
async def ans_1(call: CallbackQuery):
    await call.message.answer_document(caption="Памятка по ЛАиАГ 🤓", document=FSInputFile(
        "datas/pamyatki/[Lobanova_I.S.]_Lineinaya_algebra._Analiticheskaya(BookSee.org).pdf"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_2.callback_query(F.data == "chemistry")
async def ans_1(call: CallbackQuery):
    await call.message.answer(
        "Памятка по Химии 😍\n1.Не опаздывать 😡\n2.На ЛР носить все, что есть (готовый отчет, пз тетрадь, лк тетрадь, калькулятор, отчет распечатанный по новой теме ) 😷\n3.ДЗ на каждое ПЗ 🤗\n4. Девочкам завязывать волосы 💄\n5. Задвигать за собой стулья 👅")
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_2.callback_query(F.data == "ebriy")
async def ans_1(call: CallbackQuery):
    await call.message.answer_photo(caption="Памятка ЭБРиУ 📻", photo=types.FSInputFile("datas/pamyatki/omvpp_ebr.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_2.callback_query(F.data == "omvpp")
async def ans_1(call: CallbackQuery):
    await call.message.answer_photo(caption="Памятка ОМвПП 📻", photo=types.FSInputFile("datas/pamyatki/omvpp_ebr.jpg"))
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)


@router_2.callback_query(F.data == "oaip")
async def ans_1(call: CallbackQuery):
    await call.message.answer(
        "Памятка по ОАиП 🖥\n https://docs.google.com/spreadsheets/u/0/d/1NX7nJw71LWUjFa0NJB_9AzWzBCBU2NcdRm6cU4omGsY/htmlview#")
    buttons = InlineKeyboardMarkup(inline_keyboard=menu)
    time.sleep(3)
    await call.message.answer("Для продолжения выберете одну из функций", reply_markup=buttons)
