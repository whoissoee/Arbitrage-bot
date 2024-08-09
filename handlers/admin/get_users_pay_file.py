import os

from datetime import datetime

from aiogram.types import Message, InputFile

from keyboards.reply import AdminMenuMarkup


async def get_file(m: Message) -> None:
    await m.answer("Смотрю базу данных...")
    users_info = []
    for u_id in await m.bot["db"].get_subscribe_users_id():
        user_id = u_id["user_id"]
        username = u_id["username"]
        subscribe = u_id["subscribe"]
        date_subscribe = u_id["date_subscribe"]

        if date_subscribe and subscribe != 0:
            date_subscribe_str = datetime.strftime(date_subscribe, "%Y-%m-%d %H:%M:%S")
            date_info = f"🔰Date: {date_subscribe_str}\n"
        else:
            date_info = "" 
            
        subscribe_mapping = {
            0: "Подписки нет",
            2: "Пробная",
            10: "Дневная",
            25: "Недельная",
            75: "Месячная",
            150: "3х Месячная",
            250: "Навсегда"
        }
            
        subscribe_str = subscribe_mapping.get(subscribe, "Неизвестный тип подписки")

        user_info_str = f"🆔ID: {user_id}\n👤Username: @{username}\n✅Subs: {subscribe_str}\n{date_info}"
        
        users_info.append(user_info_str)
    
    users_formatted_str = "\n".join(users_info)
    
    await m.answer(f"Список пользователей c доступом:\n{users_formatted_str}", reply_markup=AdminMenuMarkup().get())



def setup_get_users_pay_file(dp) -> None:
    dp.register_message_handler(get_file, text=[AdminMenuMarkup.get_users_pay_file], is_admin=True)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
