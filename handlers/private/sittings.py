from aiogram.types import Message, CallbackQuery

from keyboards.reply import MainMenuMarkup
from keyboards.inline import SittingsMenuMarkup, NetworksMenuMarkup

async def ask_sittings(m: Message) -> None:
    await m.answer("⚙️ Настройки:", reply_markup=SittingsMenuMarkup().get())

async def ask_back(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    await callback_query.message.edit_text("⚙️ Настройки:", reply_markup=SittingsMenuMarkup().get())

async def ask_exit(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    chat_id = callback_query.message.chat.id
    message_id = callback_query.message.message_id
    message_id_2 = callback_query.message.message_id - 1
    await callback_query.bot.delete_message(chat_id=chat_id, message_id=message_id_2)
    await callback_query.bot.delete_message(chat_id=chat_id, message_id=message_id)

def setup_sittings(dp) -> None:
    dp.register_message_handler(ask_sittings, text=[MainMenuMarkup.settings_btn])
    dp.register_callback_query_handler(ask_back, lambda c: c.data == 'back')
    dp.register_callback_query_handler(ask_exit, lambda c: c.data == 'exit')

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
