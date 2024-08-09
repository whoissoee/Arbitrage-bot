from aiogram.types import CallbackQuery
from aiocryptopay import AioCryptoPay, Networks
import asyncio

from keyboards.inline import PriceMenuMarkup, SubscriptionMarkup
from keyboards.reply import MainMenuMarkup

#cryptopay = AioCryptoPay('160781:AAZIkKOK1TSX1YYqkIhey5tX51zvFTKK1wq', network=Networks.MAIN_NET)
cryptopay = AioCryptoPay('11512:AAx5aGI4EDf5g3WcI1A6FCMFK2qppwZf0O8', network=Networks.TEST_NET)
user_invoices = {}

async def ask_pay(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    message_text = (
        "Для начала работы нужно оплатить доступ:\n"
        "🟢24 часа - 10$\n🟢 1 неделя - 25$\n🟢 1 месяц - 75$\n"
        "🟢 3 месяца - 150$\n🟢 навсегда - 250$\n"
        "Напиши 👉 @whoissoeeS для пробного периода"
    )
    await callback_query.message.edit_text(message_text, reply_markup=PriceMenuMarkup().get())

async def ask_pay_subscribe(callback_query: CallbackQuery) -> None:
    user_id = callback_query.from_user.id
    await callback_query.answer()
    value = 0
    month = ""

    options = {
        "days": (10, "одни сутки"),
        "week": (25, "одну неделю"),
        "one_month": (75, "один месяц"),
        "three_month": (150, "три месяца"),
        "forever": (250, "навсегда"),
    }

    if callback_query.data in options:
        value, month = options[callback_query.data]
        
    check = await cryptopay.create_invoice(asset='USDT', amount=value)
    user_invoices[user_id] = check.invoice_id

    message_text = f"Чек на {value}$ для оплаты подписки на {month}"
    
    await callback_query.message.edit_text(message_text, reply_markup=SubscriptionMarkup().get(value, check.bot_invoice_url))

    timeout_minutes = 5
    check_interval_seconds = 15
    end_time = asyncio.get_event_loop().time() + timeout_minutes * 1

    while True:
        if asyncio.get_event_loop().time() > end_time:
            break

        await asyncio.sleep(check_interval_seconds)
        old_invoice = await cryptopay.get_invoices(invoice_ids=user_invoices.get(user_id))
        
    if old_invoice.status == 'paid':
        db = callback_query.bot["db"]
        await db.update_subscribe_user(value, user_id)
        success_message = f"Подписка {month} успешно оплачена!"
        await callback_query.message.edit_text(success_message, reply_markup=MainMenuMarkup().get())
    else:
        unpaid_message = f"Чек {value}$ не оплачен.\n{old_invoice}\n\n{old_invoice.status}"
        await callback_query.message.edit_text(unpaid_message)


def setup_pay(dp) -> None:

    dp.register_callback_query_handler(ask_pay, lambda c: c.data == 'pay')
    dp.register_callback_query_handler(ask_pay_subscribe, lambda c: c.data in ["days", "week", "one_month", "three_month", "forever"])


# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
