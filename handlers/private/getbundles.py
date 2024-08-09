from aiogram.types import Message, CallbackQuery
from aiogram import types
from aiogram.dispatcher import FSMContext

from keyboards.reply import MainMenuMarkup
from keyboards.inline import BundlesMenuMarkup

from concurrent.futures import ThreadPoolExecutor
from binance.client import Client
from datetime import datetime

api_key = '8nNToCd0yc8gTgHJhwM456zXUfWgLXUzSAxebqvJj5JdjTdAuzpeL30DFNsrGFeU'
api_secret = 'VFlo8h0DgE0lAhTtbG75iVAqGEw8eYKKC9cmaG05T7fZTNrSm2r7y4psj5ixnLX8'

client = Client(api_key, api_secret)

def get_ticker_info(symbol):
    ticker = client.get_ticker(symbol=symbol)
    if ticker and 'lastPrice' in ticker:
        symbol = symbol[:-4] + '/' + symbol[-4:]
        formatted_last_price = str(ticker['lastPrice']).rstrip('0').rstrip('.')
        formatted_quote_volume = str(ticker['quoteVolume']).rstrip('0').rstrip('.')
        #return f"""{symbol}"""
        return f"""
Пара {symbol}
{datetime.now().strftime("%H:%M:%S")}
Ссылка https://www.binance.com/en/trade/{ticker['symbol']}
Средний курс покупки {formatted_last_price} USDT
Объём торгов за 24ч {formatted_quote_volume} $\n"""
    return None

async def ask_bundles(m: Message, state: FSMContext) -> None:
    exchange_info = client.get_exchange_info()
    symbols = [symbol_info['symbol'] for symbol_info in exchange_info['symbols'] if "USDT" in symbol_info['symbol']]

    token_info = []
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(get_ticker_info, symbols))

    for result in results:
        if result:
            token_info.append(result)

    await state.set_data({'token_info': token_info, 'index': 0})
    await m.answer(f"{token_info[0]}", reply_markup=BundlesMenuMarkup().get(0, len(token_info), token_info), disable_web_page_preview=True)

async def ask_left_bundles(query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token_info = data.get("token_info")
    index = data.get("index")

    if index > 0:
        index -= 1
        await state.update_data(index=index)

        new_text = f'{token_info[index]}'
        
        await query.message.edit_text(new_text, reply_markup=BundlesMenuMarkup().get(index, len(token_info), token_info), disable_web_page_preview=True)
    else:
        await query.answer("End of token info list reached")

async def ask_right_bundles(query: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    token_info = data.get('token_info')
    index = data.get('index')

    if index < len(token_info):
        index += 1
        await state.update_data(index=index)

        new_text = f"{token_info[index]}"

        await query.message.edit_text(new_text, reply_markup=BundlesMenuMarkup().get(index, len(token_info), token_info), disable_web_page_preview=True)
    else:
        await query.answer("End of token info list reached")

def setup_bundles(dp) -> None:
    dp.register_callback_query_handler(ask_left_bundles, BundlesMenuMarkup.left_bundles_cb.filter(), state='*')
    dp.register_callback_query_handler(ask_right_bundles, BundlesMenuMarkup.right_bundles_cb.filter(), state='*')
    dp.register_message_handler(ask_bundles, text=[MainMenuMarkup.bundles_btn], is_premium=True, state='*')

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
