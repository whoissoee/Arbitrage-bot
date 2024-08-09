import asyncio
from datetime import datetime
from binance.client import AsyncClient

api_key = '8nNToCd0yc8gTgHJhwM456zXUfWgLXUzSAxebqvJj5JdjTdAuzpeL30DFNsrGFeU'
api_secret = 'VFlo8h0DgE0lAhTtbG75iVAqGEw8eYKKC9cmaG05T7fZTNrSm2r7y4psj5ixnLX8'

async def get_ticker_info(client, symbol):
    ticker = await client.get_ticker(symbol=symbol)
    if ticker and 'lastPrice' in ticker:
        symbol = symbol[:-4] + '/' + symbol[-4:]
        formatted_last_price = str(ticker['lastPrice']).rstrip('0').rstrip('.')
        formatted_quote_volume = str(ticker['quoteVolume']).rstrip('0').rstrip('.')
        return f"Пара: {symbol}\n{datetime.now().strftime('%H:%M:%S')}\nСсылка: https://www.binance.com/ru/trade/{ticker['symbol']}\nСредний курс покупки: {formatted_last_price} USDT\nОбъём торгов за 24ч: {formatted_quote_volume} $\n"
    return None

async def main_binance():
    client = await AsyncClient.create(api_key, api_secret)
    
    try:
        exchange_info = await client.get_exchange_info()
        symbols = [symbol_info['symbol'] for symbol_info in exchange_info['symbols'] if "USDT" in symbol_info['symbol']]

        tasks = [get_ticker_info(client, symbol) for symbol in symbols]
        results = await asyncio.gather(*tasks)

        for result in results:
            return result
    finally:
        await client.close_connection()
# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
