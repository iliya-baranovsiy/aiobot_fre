from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery

kb = [
    [InlineKeyboardButton(text="Памятки предметов 🤓", callback_data="subjects")],
    [InlineKeyboardButton(text="Описание преподов 👨‍🏫", callback_data="teachers")],
    [InlineKeyboardButton(text="Приколы 😝", callback_data="roffles")],
    [InlineKeyboardButton(text="Тест на Каяновича 🧠", callback_data="kayan_test")],
    [InlineKeyboardButton(text="Памятка Каяновича 😋", callback_data="kayn")],
    [InlineKeyboardButton(text="Вопросы к экзаменам 📖", callback_data="exes")],
    [InlineKeyboardButton(text="Проведи 1 день с химицой 💉", callback_data="chem_game")]
]

kb_1 = [
    [InlineKeyboardButton(text="МА 📊", callback_data="MA")],
    [InlineKeyboardButton(text="ЛАиАГ 📒", callback_data="laiag")],
    [InlineKeyboardButton(text="Химия 💊", callback_data="chemistry")],
    [InlineKeyboardButton(text="Эбриу 📡", callback_data="ebriy")],
    [InlineKeyboardButton(text="ОМВПП 🔌", callback_data="omvpp")],
    [InlineKeyboardButton(text="ОАиП 🖥", callback_data="oaip")],
    [InlineKeyboardButton(text="Назад", callback_data="back_1")],
]

kb_2 = [
    [InlineKeyboardButton(text="Матеша 📊", callback_data="MAs")],
    [InlineKeyboardButton(text="Химия 💊", callback_data="chemistrys")],
    [InlineKeyboardButton(text="Эбриу 📡", callback_data="ebriys")],
    [InlineKeyboardButton(text="ОМВПП 🔌", callback_data="omvpps")],
    [InlineKeyboardButton(text="ОАиП 🖥", callback_data="oaips")],
    [InlineKeyboardButton(text="Назад", callback_data="back_1")],
]

menu = [
    [InlineKeyboardButton(text="Вернуться в меню 📋", callback_data="menu")],
]

kb_exes = [
    [InlineKeyboardButton(text="ИстБГ 📙", callback_data="history")],
    [InlineKeyboardButton(text="Химия 📊", callback_data="chem_ex")],
]