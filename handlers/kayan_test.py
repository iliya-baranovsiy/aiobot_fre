import time
from aiogram import F, Router, types
from serveses.keybords import *
from serveses.states import Wait
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from serveses.functions_for_test import *

router_3 = Router()
dict_ = {}


@router_3.callback_query(F.data == "kayan_test")
async def ans_1(call: CallbackQuery, state: FSMContext):
    id = call.message.chat.id
    dict_[id] = []
    await call.message.answer(
        "Ответь на 7 вопросов и узнай на сколько % ты Каянович 😍\nВ каждом вопросе 3 варианта ответа, чтобы ответить просто введи цифру (например 1) 😜")
    await call.message.answer("Первый вопрос ✌️\nСколько будет: 'a*1' ?\n1) 1*a 👇\n2) a 👌\n3) 1 * a = a 👆")
    await state.set_state(Wait.wait_answer_1)


@router_3.message(F.text, Wait.wait_answer_1)
async def first_answer(msg: Message, state: FSMContext):
    id = msg.chat.id
    mes = msg.text
    try:
        a = first(mes)
        await msg.answer(
            "Второй вопрос ✌️\n Сколько лет Каяновичу ?\n 1) 9 математических лет 😵\n 2) 69 собачьих лет 😝\n 3) 3 человеческих годика 🤗")
        await state.set_state(Wait.wait_answer_2)
        dict_[id].append(a)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Сколько будет: 'a*1' ?\n1) 1*a 👇\n2) a 👌\n3) 1 * a = a 👆")


@router_3.message(F.text, Wait.wait_answer_2)
async def second_answer(msg: Message, state: FSMContext):
    mes = msg.text
    id = msg.chat.id
    try:
        b = second(mes)
        await msg.answer("Третий вопрос ✌️\nЧто лучше ?\n1) БГУиР 🤗\n2) МГУ 🖕\n3) ПТУ 🖕")
        await state.set_state(Wait.wait_answer_3)
        dict_[id].append(b)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer(
            "Сколько лет Каяновичу ? 🖕\n1) 9 математических лет 😵\n2) 69 собачьих лет 😝\n3) 3 человеческих годика 🤗")


@router_3.message(F.text, Wait.wait_answer_3)
async def third_answer(msg: Message, state: FSMContext):
    id = msg.chat.id
    mes = msg.text
    try:
        c = third(mes)
        await msg.answer("Четвёртый вопрос ✌️\nКто умнее ?\n1) Русские 🧔\n 2) Поляки 🤠\n 3) ФРЭ 😈")
        await state.set_state(Wait.wait_answer_4)
        dict_[id].append(c)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Что лучше ? 👙\n1) БГУиР 🤗\n 2) МГУ 🖕\n 3) ПТУ 🖕")


@router_3.message(F.text, Wait.wait_answer_4)
async def third_answer(msg: Message, state: FSMContext):
    mes = msg.text
    id = msg.chat.id
    try:
        d = four(mes)
        await msg.answer(
            "Пятый вопрос ✌️\nГде доски лучше ?\n1) Нигде ✋\n 2) Не нам этим заниматься 👳‍♂️\n 3) В пизде 🧟‍♀️")
        await state.set_state(Wait.wait_answer_5)
        dict_[id].append(d)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Кто умнее ? 🐔\n1) Русские 🧔\n 2) Поляки 🤠\n 3) ФРЭ 😈")


@router_3.message(F.text, Wait.wait_answer_5)
async def four_answer(msg: Message, state: FSMContext):
    mes = msg.text
    id = msg.chat.id
    try:
        e = five(mes)
        await msg.answer(
            "Шестой вопрос ✌️\nЧто такое шум для математика ?\n1) Смерть ☠️\n 2) Гадость 🤮\n 3) Чифир в сладость 🤗")
        await state.set_state(Wait.wait_answer_6)
        dict_[id].append(e)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Где доски лучше ? 👨‍🏫\n1) Нигде ✋\n 2) Не нам этим заниматься 👳‍♂️\n 3) В пизде 🧟‍♀️")


@router_3.message(F.text, Wait.wait_answer_6)
async def four_answer(msg: Message, state: FSMContext):
    mes = msg.text
    id = msg.chat.id
    try:
        i = six(mes)
        await msg.answer("Седьмой вопрос ✌️\nКто умнее С.С. Каяновича ?\n1) Никто 🤡\n 2) Фрэ 🤟\n 3) С.С.Каянович 🧓")
        await state.set_state(Wait.wait_answer_7)
        dict_[id].append(i)
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Что такое шум для математика ? 🚨\n1) Смерть ☠️\n 2) Гадость 🤮\n 3) Чифир в сладость 🤗")


@router_3.message(F.text, Wait.wait_answer_7)
async def four_answer(msg: Message, state: FSMContext):
    mes = msg.text
    id = msg.chat.id
    try:
        f = six(mes)
        dict_[id].append(f)
        res = count(dict_[id])
        await state.clear()
        await msg.answer("Читаю ваши ответы... 😤 ")
        time.sleep(5)
        await msg.answer_photo(caption=f"Вы на {res[0]}% С.С.Каянович 🤓", photo=types.FSInputFile(res[1]))
        buttons = InlineKeyboardMarkup(inline_keyboard=menu)
        time.sleep(2)
        await msg.answer("Для продолжения выберете одну из функций", reply_markup=buttons)
        dict_[id].clear()
    except:
        await msg.answer("Выберете номер ответа 1,2 или 3 😡")
        await msg.answer("Кто умнее С.С. Каяновича ? 🧓\n1) Никто 🤡\n 2) Фрэ 🤟\n 3) С.С.Каянович 🧓")

