from aiogram.types import CallbackQuery
from keyboards.inline import OrderSizeMenuMarkup

async def ask_order_size(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    order_size = await db.get_order_size_for_user(int(user_id))
    
    order_size_list = ' '.join([f"{c['any_size']} {c['plus_100']} {c['plus_200']} {c['plus_300']} {c['plus_500']} {c['plus_1000']}" for c in order_size])
    
    await callback_query.message.edit_text("Укажите минимальный размер покупки:", reply_markup=OrderSizeMenuMarkup().get(order_size_list))

async def ask_order_sizes(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    order_size_1 = await db.get_order_size_for_user(int(user_id))
    await db.update_order_size_for_user(callback_query.data, int(user_id))
    
    order_size_list_button = ' '.join([f"{c['any_size']} {c['plus_100']} {c['plus_200']} {c['plus_300']} {c['plus_500']} {c['plus_1000']}" for c in order_size_1])

    order_size = await db.get_order_size_for_user(int(user_id))
    order_size_list = ' '.join([f"{c['any_size']} {c['plus_100']} {c['plus_200']} {c['plus_300']} {c['plus_500']} {c['plus_1000']}" for c in order_size])

    if callback_query.data in {'any_size', 'plus_100', 'plus_200', 'plus_300', 'plus_500', 'plus_1000'}:
        index = ['any_size', 'plus_100', 'plus_200', 'plus_300', 'plus_500', 'plus_1000'].index(callback_query.data)
        if int(order_size_list_button.split(" ")[index]) != int(order_size_list.split(" ")[index]):
            await callback_query.message.edit_text("Укажите минимальный размер покупки:", reply_markup=OrderSizeMenuMarkup().get(order_size_list))

def setup_order_size(dp) -> None:
    dp.register_callback_query_handler(ask_order_size, lambda c: c.data == 'order_size')
    for size in ['any_size', 'plus_100', 'plus_200', 'plus_300', 'plus_500', 'plus_1000']:
        dp.register_callback_query_handler(ask_order_sizes, lambda c, size=size: c.data == size)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
