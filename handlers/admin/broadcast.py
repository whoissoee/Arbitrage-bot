from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes

from states.admin_states import AdminStates
from keyboards.reply import AdminCancelMarkup, AdminMenuMarkup


async def ask_broadcast_message(m: Message) -> None:
    await AdminStates.WAIT_BROADCAST_MESSAGE.set()
    await m.answer("Отправьте мне сообщение для рассылки:", reply_markup=AdminCancelMarkup().get())


async def start_broadcast(m: Message, state: FSMContext) -> None:
    await state.reset_state()
    bot = m.bot
    users = await bot["db"].get_all_users_id()
    messages_sent = 0
    await m.answer("Рассылка запущена")

    for user in users:
        try:
            await m.copy_to(user, reply_markup=m.reply_markup)
            messages_sent += 1
        except Exception as e:
            print(f"Ошибка при отправке сообщения пользователю {user}: {e}")
            continue
    await m.answer(f"Рассылка окончена.\nОтправлено сообщений: <code>{messages_sent}</code>.", parse_mode="HTML")

def setup_broadcast(dp) -> None:
    dp.register_message_handler(ask_broadcast_message, text=[AdminMenuMarkup.broadcast], is_admin=True)
    dp.register_message_handler(start_broadcast, state=AdminStates.WAIT_BROADCAST_MESSAGE,
                                content_types=ContentTypes.ANY)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
