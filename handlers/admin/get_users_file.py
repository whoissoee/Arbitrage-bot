import os

from aiogram.types import Message, InputFile

from keyboards.reply import AdminMenuMarkup


async def get_file(m: Message) -> None:
    await m.answer("Смотрю базу данных...")
    users_str=''

    for u_id in await m.bot["db"].get_all_users_id():
        users_str += f"\n{u_id}"
    await m.answer(f'Список пользователей:\n{users_str}', reply_markup=AdminMenuMarkup().get())


def setup_get_users_file(dp) -> None:
    dp.register_message_handler(get_file, text=[AdminMenuMarkup.get_users_file], is_admin=True)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
