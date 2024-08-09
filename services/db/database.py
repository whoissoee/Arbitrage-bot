import asyncpg
from datetime import datetime, timedelta
from typing import Optional, Iterable

from .models import User, SubscribeChannel, Exchange


class ConnectionsFactory:
    """ This class creates connection to the db and returns it. """
    def __init__(self, host: str, database: str, user: str, password: str):
        self.host = host
        self.database = database
        self.user = user
        self.password = password

    async def create(self) -> asyncpg.Connection:
        """ Creates database connection and returns it. """
        conn = await asyncpg.connect(
            host=self.host,
            database=self.database,
            user=self.user,
            password=self.password
        )
        return conn


class DatabaseController:
    """ Class with the all methods to working with db. """
    def __init__(self, connection):
        self._conn = connection

    async def create_db(self) -> None:
        await self._conn.execute("""CREATE TABLE IF NOT EXISTS users(
        user_id bigint,
        username varchar,
        subscribe int DEFAULT 0,
        date_subscribe TIMESTAMP 
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS channels(
        id int,
        channel_url varchar,
        channel_id bigint,
        subscribe_btn_text varchar
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS order_size(
        user_id bigint,
        any_size int DEFAULT 1,
        plus_100 int DEFAULT 0,
        plus_200 int DEFAULT 0,
        plus_300 int DEFAULT 0,
        plus_500 int DEFAULT 0,
        plus_1000 int DEFAULT 0
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS exchange (
        user_id bigint,
        binance_buy int DEFAULT 1,
        bybit_buy int DEFAULT 1,
        htx_buy int DEFAULT 1,
        mexc_buy int DEFAULT 1,
        okx_buy int DEFAULT 1,
        gateio_buy int DEFAULT 1,
        lbank_buy int DEFAULT 1,
        kucoin_buy int DEFAULT 1,
        exmo_buy int DEFAULT 1,
        bingx_buy int DEFAULT 1,
        poloniex_buy int DEFAULT 1,
        bitget_buy int DEFAULT 1,
        bitmart_buy int DEFAULT 1,
        binance_sell int DEFAULT 1,
        bybit_sell int DEFAULT 1,
        htx_sell int DEFAULT 1,
        mexc_sell int DEFAULT 1,
        okx_sell int DEFAULT 1,
        gateio_sell int DEFAULT 1,
        lbank_sell int DEFAULT 1,
        kucoin_sell int DEFAULT 1,
        exmo_sell int DEFAULT 1,
        bingx_sell int DEFAULT 1,
        poloniex_sell int DEFAULT 1,
        bitget_sell int DEFAULT 1,
        bitmart_sell int DEFAULT 1
        )""")
        
        await self._conn.execute("""CREATE TABLE IF NOT EXISTS networks(
        user_id bigint,
        any_networks int DEFAULT 1,
        bep_20 int DEFAULT 0,
        trc_20 int DEFAULT 0,                        
        erc_20 int DEFAULT 0,
        near_prot int DEFAULT 0,
        eos int DEFAULT 0,
        ava int DEFAULT 0
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS spread(
        user_id bigint,
        from_percent float DEFAULT 0.3,
        before_percent float DEFAULT 5                     
        )""")

        await self._conn.execute("""CREATE TABLE IF NOT EXISTS start(
        value_1 text,
        value_2 text                   
        )""")

    async def add_user(self, user_id: int, username: str) -> None:
        await self._conn.execute("INSERT INTO users VALUES ($1, $2)", user_id, username)
        await self._conn.execute("INSERT INTO exchange VALUES ($1)", user_id)
        await self._conn.execute("INSERT INTO order_size VALUES ($1)", user_id)
        await self._conn.execute("INSERT INTO networks VALUES ($1)", user_id)
        await self._conn.execute("INSERT INTO spread VALUES ($1)", user_id)

    async def get_user_by_id(self, user_id: int) -> Optional[User]:
        resp = await self._conn.fetchrow("SELECT * FROM users WHERE user_id=$1", user_id)
        res = None if not resp else User(user_id=resp.get("user_id"), username=resp.get("username"))
        return res

    async def get_all_users(self) -> Optional[Iterable[User]]:
        resp = await self._conn.fetch("SELECT * FROM users WHERE subscribe > 0")
        res = None if not resp else [User(user_id=u.get("user_id"), username=u.get("username")) for u in resp]
        return res

    async def get_all_users_id(self) -> Optional[Iterable[int]]:
        resp = await self._conn.fetch("SELECT user_id FROM users")
        res = None if not resp else [u.get("user_id") for u in resp]
        return res

    async def add_channel(self, channel_url: str, channel_id: int, btn_text: str) -> None:
        await self._conn.execute("INSERT INTO channels VALUES ($1, $2, $3, $4)", None, channel_url, channel_id, btn_text)

    async def delete_channel_to_subscribe_by_id(self, c_id: int) -> None:
        await self._conn.execute("DELETE FROM channels WHERE id=$1", c_id)

    async def get_all_channels_to_subscribe(self) -> Optional[Iterable[SubscribeChannel]]:
        resp = await self._conn.fetch("SELECT * FROM channels")
        if not resp:
            res = None
        else:
            res = []
            for c in resp:
                res.append(
                    SubscribeChannel(
                        id=c.get("id"),
                        channel_url=c.get("channel_url"),
                        channel_id=c.get("channel"),
                        subscribe_btn_text=c.get("subscribe_btn_text")
                    )
                )
        return res

    async def get_exchange_for_user(self, user_id: int) -> None:
        res = await self._conn.fetch("SELECT * FROM exchange WHERE user_id=$1", user_id)
        return res
    
    async def update_exchange_for_user(self, column_name, user_id: int) -> None:
        result = await self._conn.fetchrow(f"SELECT {column_name} FROM exchange WHERE user_id=$1", user_id)
        if not result[column_name]:
            new_value = 1
        else:
            new_value = 0
        query = f"UPDATE exchange SET {column_name} = $1 WHERE user_id = $2"
        await self._conn.execute(query, new_value, user_id)

    async def get_order_size_for_user(self, user_id: int) -> None:
        res = await self._conn.fetch("SELECT * FROM order_size WHERE user_id=$1", user_id)
        return res
    
    async def update_order_size_for_user(self, column_name, user_id: int) -> None:
        new_value = []
        if column_name == "any_size":
            new_value = [1, 0, 0, 0, 0, 0]
        elif column_name == "plus_100":
            new_value = [0, 1, 0, 0, 0, 0]
        elif column_name == "plus_200":
            new_value = [0, 0, 1, 0, 0, 0]
        elif column_name == "plus_300":
            new_value = [0, 0, 0, 1, 0, 0]
        elif column_name == "plus_500":
            new_value = [0, 0, 0, 0, 1, 0]
        elif column_name == "plus_1000":
            new_value = [0, 0, 0, 0, 0, 1]

        await self._conn.execute(f"UPDATE order_size SET any_size = $1, plus_100 = $2, plus_200 = $3, plus_300 = $4, plus_500 = $5, plus_1000 = $6 WHERE user_id = $7", new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[5], user_id)

    async def get_networks_for_user(self, user_id: int) -> None:
        res = await self._conn.fetch("SELECT * FROM networks WHERE user_id=$1", user_id)
        return res
    
    async def update_networks_for_user(self, column_name, user_id: int) -> None:
        new_value = []
        if column_name == "any_networks":
            new_value = [1, 0, 0, 0, 0, 0, 0]
        elif column_name == "bep_20":
            new_value = [0, 1, 0, 0, 0, 0, 0]
        elif column_name == "trc_20":
            new_value = [0, 0, 1, 0, 0, 0, 0]
        elif column_name == "erc_20":
            new_value = [0, 0, 0, 1, 0, 0, 0]
        elif column_name == "near_prot":
            new_value = [0, 0, 0, 0, 1, 0, 0]
        elif column_name == "eos":
            new_value = [0, 0, 0, 0, 0, 1, 0]
        elif column_name == "ava":
            new_value = [0, 0, 0, 0, 0, 0, 1] 


        await self._conn.execute(
            f"UPDATE networks SET any_networks = $1, bep_20 = $2, trc_20 = $3, erc_20 = $4, near_prot = $5, eos = $6, ava = $7 WHERE user_id = $8", 
            new_value[0], new_value[1], new_value[2], new_value[3], new_value[4], new_value[5], new_value[6], user_id
            )

    async def get_spread_for_user(self, user_id: int) -> None:
        res = await self._conn.fetch("SELECT * FROM spread WHERE user_id=$1", user_id)
        return res
    
    async def update_spread_for_user(self, column_name, user_id: int) -> None:
        new_value = 0

        if column_name == "left_from_percent":
            result = await self._conn.fetchval(f"SELECT from_percent FROM spread WHERE user_id = $1", user_id)
            new_value = self.calculate_new_value(result, 0.4, 1, 7.5, 20, 95)
            await self._conn.execute(f"UPDATE spread SET from_percent = $1 WHERE user_id = $2", new_value, user_id)

        elif column_name == "right_from_percent":
            result = await self._conn.fetchval(f"SELECT from_percent FROM spread WHERE user_id = $1", user_id)
            new_value = self.calculate_new_value(result, 0.3, 1, 7.5, 20, 100)
            await self._conn.execute(f"UPDATE spread SET from_percent = $1 WHERE user_id = $2", new_value, user_id)

        elif column_name == "left_before_percent":
            result = await self._conn.fetchval(f"SELECT before_percent FROM spread WHERE user_id = $1", user_id)
            new_value = self.calculate_new_value(result, 0.5, 1, 7.5, 20, 100)
            await self._conn.execute(f"UPDATE spread SET before_percent = $1 WHERE user_id = $2", new_value, user_id)

        elif column_name == "right_before_percent":
            result = await self._conn.fetchval(f"SELECT before_percent FROM spread WHERE user_id = $1", user_id)
            new_value = self.calculate_new_value(result, 0.4, 1, 7.5, 20, 100)
            await self._conn.execute(f"UPDATE spread SET before_percent = $1 WHERE user_id = $2", new_value, user_id)

    def calculate_new_value(self, result, *intervals):
        for i in range(len(intervals) - 1):
            if intervals[i] <= result < intervals[i + 1]:
                return result - (0.1 * i) if i < 4 else result - 5
        return result

    async def update_subscribe_user(self, value, user_id: int) -> None:
        current_datetime = datetime.now()
        await self._conn.execute("UPDATE users SET subscribe = $1, date_subscribe = $2 WHERE user_id = $3",value, current_datetime, user_id)

    async def get_premium_for_user(self, user_id: int) -> bool:
        row = await self._conn.fetchrow("SELECT subscribe, date_subscribe FROM users WHERE user_id = $1", user_id)
        
        if row:
            result, date = row['subscribe'], row['date_subscribe']
            current_time = datetime.now()
            
            # Определение временных интервалов
            two_hours_ago = current_time - timedelta(hours=2)
            days_ago = current_time - timedelta(days=1)
            weeks_ago = current_time - timedelta(weeks=1)
            one_month_ago = current_time - timedelta(days=30)
            three_month_ago = current_time - timedelta(days=91)
            
            # Проверка условий премиум-статуса
            if result == 2 and date > two_hours_ago:
                return True
            elif result == 10 and date > days_ago:
                return True
            elif result == 25 and date > weeks_ago:
                return True
            elif result == 75 and date > one_month_ago:
                return True
            elif result == 150 and date > three_month_ago:
                return True
            elif result == 250:
                return True
            elif result == 0:
                return False
        
        return False
        
    async def get_values_start_message(self) -> tuple:
        result = await self._conn.fetchrow("SELECT value_1, value_2 FROM start") 
        return result
    
    async def update_start_message(self, text_1, text_2) -> None:
        existing_data = await self._conn.fetchrow("SELECT * FROM start")
        
        if existing_data:
            await self._conn.execute("""
            UPDATE start
            SET value_1 = $1, value_2 = $2
            """, text_1, text_2)
        else:
            await self._conn.execute("""
            INSERT INTO start (value_1, value_2)
            VALUES ($1, $2)
            """, text_1, text_2)


    async def get_subscribe_users_id(self) -> None:
        res = await self._conn.fetch("SELECT user_id, username, subscribe, date_subscribe FROM users")
        return res

    async def disconnect(self) -> None:
        await self._conn.close()

# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
