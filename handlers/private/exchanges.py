from aiogram.types import CallbackQuery
from keyboards.inline import ExchangesMenuMarkup

async def ask_exchanges(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    exchange_list = await get_exchange_list(db, user_id)
    
    await callback_query.message.edit_text(
        "Укажите нужные биржи для покупки/продажи:",
        reply_markup=ExchangesMenuMarkup().get(exchange_list)
    )

async def ask_exchange(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    selected_exchange = callback_query.data
    
    await db.update_exchange_for_user(selected_exchange, int(user_id))
    
    exchange_list = await get_exchange_list(db, user_id)
    
    await callback_query.message.edit_text(
        "Укажите нужные биржи для покупки/продажи:",
        reply_markup=ExchangesMenuMarkup().get(exchange_list)
    )

async def get_exchange_list(db, user_id):
    exchange = await db.get_exchange_for_user(int(user_id))
    for c in exchange:
        return " ".join(f"{c['binance_buy']} {c['bybit_buy']} {c['htx_buy']} {c['mexc_buy']} {c['okx_buy']} {c['gateio_buy']} {c['lbank_buy']} {c['kucoin_buy']} {c['exmo_buy']} {c['bingx_buy']} {c['poloniex_buy']} {c['bitget_buy']} {c['bitmart_buy']} {c['binance_sell']} {c['bybit_sell']} {c['htx_sell']} {c['mexc_sell']} {c['okx_sell']} {c['gateio_sell']} {c['lbank_sell']} {c['kucoin_sell']} {c['exmo_sell']} {c['bingx_sell']} {c['poloniex_sell']} {c['bitget_sell']} {c['bitmart_sell']}")

def setup_exchanges(dp) -> None:
    dp.register_callback_query_handler(ask_exchanges, lambda c: c.data == 'exchanges')
    
    exchanges = ["binance_buy", "bybit_buy", "htx_buy", "mexc_buy", "okx_buy", "gateio_buy", "lbank_buy", "kucoin_buy", "exmo_buy", "bingx_buy", "poloniex_buy", "bitget_buy", "bitmart_buy", "binance_sell", "bybit_sell", "htx_sell", "mexc_sell", "okx_sell", "gateio_sell", "lbank_sell", "kucoin_sell", "exmo_sell", "bingx_sell", "poloniex_sell", "bitget_sell", "bitmart_sell"]
    
    for exchange in exchanges:
        dp.register_callback_query_handler(ask_exchange, lambda c, exchange=exchange: c.data == exchange)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
