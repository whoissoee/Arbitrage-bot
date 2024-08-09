from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes

from states.admin_states import AdminStates
from keyboards.reply import AdminCancelMarkup, AdminMenuMarkup

async def show_start_message(m: Message):
    await AdminStates.WAIT_UPDATE_MSG.set()
    await m.answer("Пожалуйста, напишите новое приветственное сообщение или нажмите на кнопку \"🆕 Изменить приветствие\"", reply_markup=AdminCancelMarkup().get())

async def update_value_start_message_step1(m: Message, state: FSMContext):
    text_1=m.text
    await state.update_data(text_1=text_1)
    await m.answer("Отлично! Теперь напишите текст, на который вы хотите заменить приветственное сообщение.")
    await AdminStates.WAIT_UPDATE_MSG2.set()

async def update_value_start_message_step2(m: Message, state: FSMContext):
    data = await state.get_data()
    text_1 = data.get("text_1")
    text_2 = m.text
    bot = m.bot
    await bot["db"].update_start_message(text_1, text_2)
    await m.answer(f"Приветственное сообщение успешно обновлено на:\n{text_1}\n{text_2}", reply_markup=AdminMenuMarkup().get())
    await state.finish()

def setup_update_message(dp) -> None:
    dp.register_message_handler(show_start_message, text=[AdminMenuMarkup.change], is_admin=True)
    dp.register_message_handler(update_value_start_message_step1, state=AdminStates.WAIT_UPDATE_MSG, content_types=ContentTypes.ANY, is_admin=True)
    dp.register_message_handler(update_value_start_message_step2, state=AdminStates.WAIT_UPDATE_MSG2, content_types=ContentTypes.ANY, is_admin=True)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
