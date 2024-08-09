from aiogram.types import Message, ChatType
from aiogram.dispatcher.filters import ChatTypeFilter

from keyboards.inline import PayMenuMarkup
from keyboards.reply import MainMenuMarkup

async def start_msg(m: Message) -> None:
    reply_markup = MainMenuMarkup().get()
    db = m.bot["db"]
    values = await db.get_values_start_message()  
    
    if values:
        value_1, value_2 = values
    else:
        value_1 = "___________________"
        value_2 = "___________________"
    await m.answer(f'{value_1}\n\n💱 Доступные биржи:\n - <a href="https://www.binance.com/" target="_blank">Binance</a>\n - <a href="https://www.bybit.com//" target="_blank">ByBit</a>\n - <a href="https://www.bingx.com/" target="_blank">BingX</a>\n - <a href="https://www.kucoin.com/" target="_blank">Kucoin</a>\n - <a href="https://www.mexc.com/" target="_blank">Mexc</a>\n - <a href="https://www.gate.io/" target="_blank">Gate.io</a>\n - <a href="https://www.okx.com/" target="_blank">Okx</a>\n - <a href="https://www.bitget.com/" target="_blank">Bitget</a>\n - <a href="https://www.lbank.info/" target="_blank">Lbank</a>\n - <a href="https://www.poloniex.com/" target="_blank">Poloniex</a>\n - <a href="https://www.exmo.com/" target="_blank">Exmo</a>\n\n{value_2}', reply_markup=reply_markup, parse_mode="HTML", disable_web_page_preview=True)

def setup_start(dp) -> None:
    dp.register_message_handler(lambda m: start_msg(m), ChatTypeFilter(ChatType.PRIVATE), is_premium=True, commands=["start"])


# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
