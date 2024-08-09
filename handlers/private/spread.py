from aiogram.types import CallbackQuery
from keyboards.inline import SpreadMenuMarkup

async def ask_spread(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    spread_list = ""
    spread = await db.get_spread_for_user(int(user_id))
    
    for c in spread:
        from_percent = float(c['from_percent'])
        before_percent = float(c['before_percent'])
        spread_list += f"{from_percent} {before_percent} "
    await callback_query.message.edit_text("Укажите нужный процент связки:", reply_markup=SpreadMenuMarkup().get(spread_list))
async def ask_spreads(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    spread_1 = await db.get_spread_for_user(int(user_id))

    spread_list_button = ""
    for c in spread_1:
        from_percent = float(c['from_percent'])
        before_percent = float(c['before_percent'])
        spread_list_button += f"{from_percent} {before_percent} "

    if float(spread_list_button.split(" ")[0]) < float(spread_list_button.split(" ")[1]):
        await db.update_spread_for_user(callback_query.data, int(user_id))
        
        spread_2 = await db.get_spread_for_user(int(user_id))
        spread_list = ""
        for c in spread_2:
            from_percent = float(c['from_percent'])
            before_percent = float(c['before_percent'])
            spread_list += f"{from_percent} {before_percent} "

        if callback_query.data == 'left_from_percent' and float(spread_list.split(" ")[0]) > 0.3:
            await callback_query.message.edit_text("Укажите нужный процент связки:", reply_markup=SpreadMenuMarkup().get(spread_list))
        elif callback_query.data == 'right_from_percent' and float(spread_list.split(" ")[0]) < 95.0:
            await callback_query.message.edit_text("Укажите нужный процент связки:", reply_markup=SpreadMenuMarkup().get(spread_list))
        elif callback_query.data == 'left_before_percent' and float(spread_list.split(" ")[1]) > 0.4:
            await callback_query.message.edit_text("Укажите нужный процент связки:", reply_markup=SpreadMenuMarkup().get(spread_list))
        elif callback_query.data == 'right_before_percent' and float(spread_list.split(" ")[1]) < 100.0:
            await callback_query.message.edit_text("Укажите нужный процент связки:", reply_markup=SpreadMenuMarkup().get(spread_list))


def setup_spread(dp) -> None:
    dp.register_callback_query_handler(ask_spread, lambda c: c.data == 'spread')
    dp.register_callback_query_handler(ask_spreads, lambda c: c.data in ["left_from_percent", "right_from_percent", "left_before_percent", "right_before_percent"])

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
