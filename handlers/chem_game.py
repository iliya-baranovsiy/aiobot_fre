from aiogram import F, Router, types
from serveses.keybords import *
from serveses.states import Wait
from aiogram.fsm.context import FSMContext
from aiogram.types import Message
from serveses.function_chem import *
import time

router_5 = Router()


@router_5.callback_query(F.data == "chem_game")
async def first(call: CallbackQuery, state: FSMContext):
    await call.message.answer_photo(
        caption="Привет, ты попал в настоящее выживание c химицей ☠️.\nУ тебя всего лишь одна жизнь, а значит тебе нельзя допускать ошибку 😵.\nПравила:\n1) Анна Ивановна - друг 🙋‍♀️\n2) Пробирки только для реактивов 💣\n3) Соль нюхать нельзя 🧟‍♂️\n4) отвечать только 1,2 или 3 🎯",
        photo=types.FSInputFile("datas/for_chem/chem.png"))
    time.sleep(5)
    await call.message.answer(
        "Эпизод 1 ☠️:\nК тебе подошла Анна Ивановна, твои действия ? 🤯\n1) Прогнать\n2) Выслушать\n3) Заплакать")
    await state.set_state(Wait.wait_answer_chem_1)


@router_5.message(F.text, Wait.wait_answer_chem_1)
async def second(msg: Message, state: FSMContext):
    mes = msg.text
    try:
        ans = first_chem(mes)
        if ans == "OK":
            await msg.answer(
                "Эпизод 2 ☠️:\nТы увидел белый порошок на парте, что будешь делать ? 😍\n1) Занюхнёшь в две ноздри\n2)Занюхнешь в одну ноздрю\n3) Стряхнёшь на пол")
            await state.set_state(Wait.wait_answer_chem_2)
        else:
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer("Химица увидела это 🙀. Ты проиграл вернись в меню ", reply_markup=buttons)
            await state.clear()
    except:
        await msg.answer("Отвечай только данными ответами, или ты хочешь проиграть ? 🤬")
        await  msg.answer("К тебе подошла Анна Ивановна, твои действия ? 🤯\n1) Прогнать\n2) Выслушать\n3) Заплакать")


@router_5.message(F.text, Wait.wait_answer_chem_2)
async def third(msg: Message, state: FSMContext):
    mes = msg.text
    try:
        ans = second_chem(mes)
        if ans == "OK":
            await msg.answer(
                "Эпизод 3 ☠️:\nТы решил списать контрольную, как ты это сделаешь ? 😷\n1) Подзову Анну Ивановну\n2) Достану шпоры\n3) Буду звать отличников на помощь")
            await state.set_state(Wait.wait_answer_chem_3)
        else:
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer("Это была соль и ты обдолбался 😤. Вернись в меню", reply_markup=buttons)
            await state.clear()
    except:
        await msg.answer("Отвечай только данными ответами, или ты хочешь проиграть ? 🤬")
        await  msg.answer(
            "Ты увидел белый порошок на парте, что будешь делать ? 😍\n1) Занюхнёшь в две ноздри\n2)Занюхнешь в одну ноздрю\n3) Стряхнёшь на пол")


@router_5.message(F.text, Wait.wait_answer_chem_3)
async def fourth(msg: Message, state: FSMContext):
    mes = msg.text
    try:
        ans = third_chem(mes)
        if ans == "OK":
            await msg.answer(
                "Эпизод 4 ☠️:\nТы увидел пробирку с прозрачным веществом, твои действия ? 😼\n1) Просто понюхаю\n2) Выпью\n3) Спрошу что это")
            await state.set_state(Wait.wait_answer_chem_4)
        else:
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer("Тебя заметили 🖕, вернись в меню", reply_markup=buttons)
            await state.clear()
    except:
        await msg.answer("Отвечай только данными ответами, или ты хочешь проиграть ? 🤬")
        await  msg.answer(
            "Ты решил списать контрольную, как ты это сделаешь ? 😷\n1) Подзову Анну Ивановну\n2) Достану шпоры\n3) Буду звать отличников на помощь")


@router_5.message(F.text, Wait.wait_answer_chem_4)
async def fourth(msg: Message, state: FSMContext):
    mes = msg.text
    try:
        ans = four_chem(mes)
        if ans == "OK":
            await msg.answer(
                "Эпизод 5 ☠️:\nТы захотел дать газу, что будешь делать? 🐖\n1) Сдержусь\n2) Дам по-полной\n3) Дам как мышка")
            await state.set_state(Wait.wait_answer_chem_5)
        elif ans == "Ok_1":
            await msg.answer("Ты выжил, но в ответ услышал 'А тебя это ебать не должно 🙈'")
            await msg.answer(
                "Эпизод 5 ☠️:\nТы захотел дать газу, что будешь делать? 🐖\n1) Сдержусь\n2) Дам по-полной\n3) Дам как мышка")
            await state.set_state(Wait.wait_answer_chem_5)
        else:
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer("Это был яд ☠️ ты умер", reply_markup=buttons)
            await state.clear()
    except:
        await msg.answer("Отвечай только данными ответами, или ты хочешь проиграть ? 🤬")
        await  msg.answer(
            "Ты увидел пробирку с прозрачным веществом, твои действия ? 😼\n1) Просто понюхаю\n2) Выпью\n3) Спрошу что это")


@router_5.message(F.text, Wait.wait_answer_chem_5)
async def fourth(msg: Message, state: FSMContext):
    mes = msg.text
    try:
        ans = five_chem(mes)
        if ans == "OK":
            await state.clear()
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer_photo(
                caption="Мои поздравления, теперь ты достоин звания сталкера фрэ 🎖🎖🎖\nВозвращайся в меню меченый",photo=types.FSInputFile("datas/for_chem/i.jpg"))
            await msg.answer("Вернуться в меню",reply_markup=buttons)
        else:
            buttons = InlineKeyboardMarkup(inline_keyboard=menu)
            await msg.answer("Задохнулись все в радиусе 5 километров 🚷, возвращайся в меню ", reply_markup=buttons)
            await state.clear()
    except:
        await msg.answer("Отвечай только данными ответами, или ты хочешь проиграть ? 🤬")
        await  msg.answer("Ты захотел дать газу, что будешь делать? 🐖\n1) Сдержусь\n2) Дам по-полной\n3) Дам как мышка")


@router_5.message()
async def next_message(msg: Message):
    buttons = InlineKeyboardMarkup(inline_keyboard=kb)
    await msg.answer("Для продолжения выберете одну из функций 👇", reply_markup=buttons)
