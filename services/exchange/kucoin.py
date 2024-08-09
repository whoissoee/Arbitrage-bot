import aiohttp
import asyncio
from datetime import datetime

async def get_ticker_data(session, symbol):
    ticker_url = f"https://api.kucoin.com/api/v1/market/stats?symbol={symbol}"
    async with session.get(ticker_url) as ticker_response:
        ticker_data = await ticker_response.json()
        
        if "data" in ticker_data:
            last_price = ticker_data["data"]["last"]
            volume_24h = ticker_data["data"]["vol"]
            return last_price, volume_24h
        else:
            return None, None

async def process_symbol(session, symbol):
    symbol_pair = symbol[:-5] + "/" + symbol[-4:]
    last_price, volume_24h = await get_ticker_data(session, symbol)
    
    if last_price is not None and volume_24h is not None:
        result = f"Пара: {symbol_pair}\n{datetime.now().strftime('%H:%M:%S')}\nСсылка: https://www.kucoin.com/ru/trade/{symbol}\nСредний курс покупки: {last_price} USDT\nОбъём торгов за 24ч: {volume_24h}$"
        return result
    else:
        return None

async def main():
    symbols_url = "https://api.kucoin.com/api/v1/symbols"
    async with aiohttp.ClientSession() as session:
        symbols_response = await session.get(symbols_url)
        symbols_result = await symbols_response.json()

        results = []

        tasks = [process_symbol(session, i["symbol"]) for i in symbols_result["data"] if "USDT" in i["symbol"]]
        results = await asyncio.gather(*tasks)

        for result in results:
            return result
# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
