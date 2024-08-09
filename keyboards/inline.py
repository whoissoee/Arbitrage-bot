from aiogram.utils.callback_data import CallbackData
from utils import InlineMarkupConstructor

class PayMenuMarkup(InlineMarkupConstructor):
    pay_cb = CallbackData("pay")

    def get(self):
        schema = [1]

        actions = [
            {"text": "Оформить подписку", "cb": self.pay_cb.new()},
        ]
        return self.markup(actions, schema)

class ChannelsToSubscribeKb(InlineMarkupConstructor):
    check_sub_cb = CallbackData("check_sub")

    def get(self, channels_data_list: list):
        schema = []
        actions = []
        for c in channels_data_list:
            schema.append(1)
            actions.append({"text": c[1], "url": c[0]})
        schema.append(1)
        actions.append({"text": "Проверить подписку", "cb": self.check_sub_cb.new()})
        return self.markup(actions, schema)

class PriceMenuMarkup(InlineMarkupConstructor):
    days_cb = CallbackData("days")
    week_cb = CallbackData("week")
    one_month_cb = CallbackData("one_month")
    three_month_cb = CallbackData("three_month")
    forever_cb = CallbackData("forever")

    def get(self):
        schema = [1, 1, 1, 1, 1]

        actions = [
            {"text": "Оплатить 10$", "cb": self.days_cb.new()},
            {"text": "Оплатить 25$", "cb": self.week_cb.new()},
            {"text": "Оплатить 75$", "cb": self.one_month_cb.new()},
            {"text": "Оплатить 150$", "cb": self.three_month_cb.new()},
            {"text": "Оплатить 250$", "cb": self.forever_cb.new()},
        ]
        return self.markup(actions, schema)
    
class SubscriptionMarkup(InlineMarkupConstructor):
    def get(self, value, check_url):
        schema = [1]

        actions = [
            {"text": f"Оплатить {value}$", "url": check_url},
        ]
        return self.markup(actions, schema)
    
class SittingsMenuMarkup(InlineMarkupConstructor):
    exchanges_cb = CallbackData("exchanges")
    networks_cb = CallbackData("networks")
    spread_cb = CallbackData("spread")
    order_size_cb = CallbackData("order_size")
    exit_cb = CallbackData("exit")

    def get(self):
        schema = [2, 2, 1]

        actions = [
            {"text": "💱 Биржи", "cb": self.exchanges_cb.new()},
            {"text": "🌐 Сети", "cb": self.networks_cb.new()},
            {"text": "💵 Спред", "cb": self.spread_cb.new()},
            {"text": "💲 Размер ордера", "cb": self.order_size_cb.new()},
            {"text": "❌ Выйти", "cb": self.exit_cb.new()},
        ]
        return self.markup(actions, schema)
    
class SpreadMenuMarkup(InlineMarkupConstructor):
    from_cb = CallbackData("from")
    left_from_cb = CallbackData("left_from_percent")
    percent_from_cb = CallbackData("percent_from")
    right_from_cb = CallbackData("right_from_percent")
    before_cb = CallbackData("before")
    left_before_cb = CallbackData("left_before_percent")
    percent_before_cb = CallbackData("percent_before")
    right_before_cb = CallbackData("right_before_percent")
    back_cb = CallbackData("back")
    exit_cb = CallbackData("exit")


    def get(self, for_data):
        schema = [1, 3, 1, 3, 1, 1]
        actions = [
            {"text": "От:", "cb": self.from_cb.new()},
            {"text": "⬅️", "cb": self.left_from_cb.new()},
            {"text": f"{for_data.split(' ')[0]} %", "cb": self.percent_from_cb.new()},
            {"text": "➡️", "cb": self.right_from_cb.new()},
            {"text": "До:", "cb": self.before_cb.new()},
            {"text": "⬅️", "cb": self.left_before_cb.new()},
            {"text": f"{for_data.split(' ')[1]} %", "cb": self.percent_before_cb.new()},
            {"text": "➡️", "cb": self.right_before_cb.new()},
            {"text": "⬅️ Назад", "cb": self.back_cb.new()},
            {"text": "❌ Выйти", "cb": self.exit_cb.new()}
        ]
        return self.markup(actions, schema)

class NetworksMenuMarkup(InlineMarkupConstructor):
    any_networks_cb = CallbackData("any_networks")
    bep_cb = CallbackData("bep_20")
    trc_cb = CallbackData("trc_20")
    erc_cb = CallbackData("erc_20")
    near_cb = CallbackData("near_prot")
    eos_cb = CallbackData("eos")
    avax_cb = CallbackData("ava")
    back_cb = CallbackData("back")
    exit_cb = CallbackData("exit")


    def get(self, for_data):
        schema = [1, 3, 3, 1, 1]

        data = []
        for value in for_data.split():
            if value == '1':
                data.append("✅ ")
            elif value == '0':
                data.append("")
            else:
                data.append("ошибка ")

        actions = [
            {"text": f"{data[0]} any", "cb": self.any_networks_cb.new()},
            {"text": f"{data[1]} BEP-20", "cb": self.bep_cb.new()},
            {"text": f"{data[2]} TRC-20", "cb": self.trc_cb.new()},
            {"text": f"{data[3]} ERC-20", "cb": self.erc_cb.new()},
            {"text": f"{data[4]} Near", "cb": self.near_cb.new()},
            {"text": f"{data[5]} EOS", "cb": self.eos_cb.new()},
            {"text": f"{data[6]} AVAX", "cb": self.avax_cb.new()},
            {"text": "⬅️ Назад", "cb": self.back_cb.new()},
            {"text": "❌ Выйти", "cb": self.exit_cb.new()},
        ]
        return self.markup(actions, schema)
    
class BundlesMenuMarkup(InlineMarkupConstructor):
    left_bundles_cb = CallbackData("left_bundles", "page", "pages")
    page_bundles_cb = CallbackData("page_bundles", "page", "pages")
    right_bundles_cb = CallbackData("right_bundles", "page", "pages")

    def get(self, page, pages, token_info):
        schema = [3]

        actions = [
            {"text": f"⬅️", "cb": self.left_bundles_cb.new(page=page, pages=pages)},
            {"text": f"{page}/{pages}", "cb": self.page_bundles_cb.new(page=page, pages=pages)},
            {"text": f"➡️", "cb": self.right_bundles_cb.new(page=page, pages=pages)}
        ]
        return self.markup(actions, schema)

class OrderSizeMenuMarkup(InlineMarkupConstructor):
    any_size_cb = CallbackData("any_size")
    plus_100_cb = CallbackData("plus_100")
    plus_200_cb = CallbackData("plus_200")
    plus_300_cb = CallbackData("plus_300")
    plus_500_cb = CallbackData("plus_500")
    plus_1000_cb = CallbackData("plus_1000")
    back_cb = CallbackData("back")
    exit_cb = CallbackData("exit")


    def get(self, for_data):
        schema = [1, 3, 2, 1, 1]

        data = []
        for value in for_data.split():
            if value == '1':
                data.append("✅ ")
            elif value == '0':
                data.append("")
            else:
                data.append("ошибка ")

        actions = [
            {"text": f"{data[0]} any", "cb": self.any_size_cb.new()},
            {"text": f"{data[1]} 100+", "cb": self.plus_100_cb.new()},
            {"text": f"{data[2]} 200+", "cb": self.plus_200_cb.new()},
            {"text": f"{data[3]} 300+", "cb": self.plus_300_cb.new()},
            {"text": f"{data[4]} 500+", "cb": self.plus_500_cb.new()},
            {"text": f"{data[5]} 1000+", "cb": self.plus_1000_cb.new()},
            {"text": "⬅️ Назад", "cb": self.back_cb.new()},
            {"text": "❌ Выйти", "cb": self.exit_cb.new()},
        ]
        return self.markup(actions, schema)

class ExchangesMenuMarkup(InlineMarkupConstructor):
    buy_cb = CallbackData("_buy")
    binance_buy_cb = CallbackData("binance_buy")
    bybit_buy_cb = CallbackData("bybit_buy")
    htx_buy_cb = CallbackData("htx_buy")
    mexc_buy_cb = CallbackData("mexc_buy")
    okx_buy_cb = CallbackData("okx_buy")
    gateio_buy_cb = CallbackData("gateio_buy")
    lbank_buy_cb = CallbackData("lbank_buy")
    kucoin_buy_cb = CallbackData("kucoin_buy")
    exmo_buy_cb = CallbackData("exmo_buy")
    bingx_buy_cb = CallbackData("bingx_buy")
    poloniex_buy_cb = CallbackData("poloniex_buy")
    bitget_buy_cb = CallbackData("bitget_buy")
    bitmart_buy_cb = CallbackData("bitmart_buy")
    sell_cb = CallbackData("_sell")
    binance_sell_cb = CallbackData("binance_sell")
    bybit_sell_cb = CallbackData("bybit_sell")
    htx_sell_cb = CallbackData("htx_sell")
    mexc_sell_cb = CallbackData("mexc_sell")
    okx_sell_cb = CallbackData("okx_sell")
    gateio_sell_cb = CallbackData("gateio_sell")
    lbank_sell_cb = CallbackData("lbank_sell")
    kucoin_sell_cb = CallbackData("kucoin_sell")
    exmo_sell_cb = CallbackData("exmo_sell")
    bingx_sell_cb = CallbackData("bingx_sell")
    poloniex_sell_cb = CallbackData("poloniex_sell")
    bitget_sell_cb = CallbackData("bitget_sell")
    bitmart_sell_cb = CallbackData("bitmart_sell")
    back_cb = CallbackData("back")
    exit_cb = CallbackData("exit")

    def get(self, for_data):
        schema = [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1]

        data = []
        for value in for_data.split():
            if value == '1':
                data.append("✅ ")
            elif value == '0':
                data.append("❌ ")
            else:
                data.append("ошибка ")


        actions = [
            {"text": "Покупка", "cb": self.buy_cb.new()},
            {"text": "Продажа", "cb": self.sell_cb.new()},
            {"text": f"{data[0]} Binance", "cb": self.binance_buy_cb.new()},
            {"text": f"{data[13]} Binance", "cb": self.binance_sell_cb.new()},
            {"text": f"{data[1]} Bybit", "cb": self.bybit_buy_cb.new()},
            {"text": f"{data[14]} Bybit", "cb": self.bybit_sell_cb.new()},
            {"text": f"{data[2]} Htx", "cb": self.htx_buy_cb.new()},
            {"text": f"{data[15]} Htx", "cb": self.htx_sell_cb.new()},
            {"text": f"{data[3]} Mexc", "cb": self.mexc_buy_cb.new()},
            {"text": f"{data[16]} Mexc", "cb": self.mexc_sell_cb.new()},
            {"text": f"{data[4]} Okx", "cb": self.okx_buy_cb.new()},
            {"text": f"{data[17]} Okx", "cb": self.okx_sell_cb.new()},
            {"text": f"{data[5]} Gate.io", "cb": self.gateio_buy_cb.new()},
            {"text": f"{data[18]} Gate.io", "cb": self.gateio_sell_cb.new()},
            {"text": f"{data[6]} LBank", "cb": self.lbank_buy_cb.new()},
            {"text": f"{data[19]} LBank", "cb": self.lbank_sell_cb.new()},
            {"text": f"{data[7]} Kucoin", "cb": self.kucoin_buy_cb.new()},
            {"text": f"{data[20]} Kucoin", "cb": self.kucoin_sell_cb.new()},
            {"text": f"{data[8]} Exmo", "cb": self.exmo_buy_cb.new()},
            {"text": f"{data[21]} Exmo", "cb": self.exmo_sell_cb.new()},
            {"text": f"{data[9]} BingX", "cb": self.bingx_buy_cb.new()},
            {"text": f"{data[22]} BingX", "cb": self.bingx_sell_cb.new()},
            {"text": f"{data[10]} Poloniex", "cb": self.poloniex_buy_cb.new()},
            {"text": f"{data[23]} Poloniex", "cb": self.poloniex_sell_cb.new()},
            {"text": f"{data[11]} BitGet", "cb": self.bitget_buy_cb.new()},
            {"text": f"{data[24]} BitGet", "cb": self.bitget_sell_cb.new()},
            {"text": f"{data[12]} Bitmart", "cb": self.bitmart_buy_cb.new()},
            {"text": f"{data[25]} Bitmart", "cb": self.bitmart_sell_cb.new()},
            {"text": "⬅️ Назад", "cb": self.back_cb.new()},
            {"text": "❌ Выйти", "cb": self.exit_cb.new()},
        ]
        return self.markup(actions, schema)

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
