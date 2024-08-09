from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes

from states.admin_states import AdminStates
from keyboards.reply import AdminCancelMarkup, AdminMenuMarkup


async def ask_user_id_message(m: Message) -> None:
    await AdminStates.WAIT_USER_ID_MESSAGE.set()
    await m.answer("Отправьте мне user_id пользователя для выдачи двух часового доступа:", reply_markup=AdminCancelMarkup().get())


async def start_free_work(m: Message, state: FSMContext) -> None:
    await state.reset_state()
    bot = m.bot
    user_id = m.text
    result = await bot["db"].get_all_users_id()
    if int(user_id) in result:
        await bot["db"].update_subscribe_user(2, int(user_id))
        await m.answer(f"{user_id} получил двух часовой доступ.", reply_markup=AdminMenuMarkup().get())
    else:
        await m.answer(f"Пользователь с ID {user_id} не найден.", reply_markup=AdminMenuMarkup().get())

def setup_free_work(dp) -> None:
    dp.register_message_handler(ask_user_id_message, text=[AdminMenuMarkup.two_hours_work], is_admin=True)
    dp.register_message_handler(start_free_work, state=AdminStates.WAIT_USER_ID_MESSAGE,
                                content_types=ContentTypes.ANY)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
