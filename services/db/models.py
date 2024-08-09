from dataclasses import dataclass


@dataclass
class User:
    user_id: int
    username: str

@dataclass
class SubscribeChannel:
    id: int
    channel_url: str
    channel_id: str
    subscribe_btn_text: str

@dataclass
class Exchange:
    user_id: int
    binance_buy: int
    bybit_buy: int
    htx_buy: int
    mexc_buy: int
    okx_buy: int
    gateio_buy: int
    lbank_buy: int
    kucoin_buy: int
    exmo_buy: int
    bingx_buy: int
    poloniex_buy: int
    bitget_buy: int
    bitmart_buy: int
    binance_sell: int
    bybit_sell: int
    htx_sell: int
    mexc_sell: int
    okx_sell: int
    gateio_sell: int
    lbank_sell: int
    kucoin_sell: int
    exmo_sell: int
    bingx_sell: int
    poloniex_sell: int
    bitget_sell: int
    bitmart_sell: int

@dataclass
class OrderSize:
    user_id: int
    any_size: int
    plus_100: int
    plus_200: int
    plus_300: int
    plus_500: int

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
