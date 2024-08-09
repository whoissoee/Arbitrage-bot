from aiogram.types import Message

from keyboards.reply import AdminMenuMarkup


async def check_users_count(m: Message) -> None:
    users = await m.bot["db"].get_all_users_id()
    await m.answer(f"Пользователей в бд: {len(users)}")


def setup_check_users(dp) -> None:
    dp.register_message_handler(check_users_count, text=[AdminMenuMarkup.check_users], is_admin=True)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
