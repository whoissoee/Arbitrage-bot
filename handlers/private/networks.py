from aiogram.types import CallbackQuery
from keyboards.inline import NetworksMenuMarkup

async def ask_networks(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    networks = await db.get_networks_for_user(int(user_id))

    networks_list = " ".join(f"{c['any_networks']} {c['bep_20']} {c['trc_20']} {c['erc_20']} {c['near_prot']} {c['eos']} {c['ava']}" for c in networks)
    await callback_query.message.edit_text("Укажите сеть в связке для вывода:", reply_markup=NetworksMenuMarkup().get(networks_list))

async def ask_network(callback_query: CallbackQuery) -> None:
    await callback_query.answer()
    db = callback_query.bot["db"]
    user_id = callback_query.message.chat.id
    networks_before_update = await db.get_networks_for_user(int(user_id))
    await db.update_networks_for_user(callback_query.data, int(user_id))
    networks_after_update = await db.get_networks_for_user(int(user_id))

    networks_list_button = " ".join(f"{c['any_networks']} {c['bep_20']} {c['trc_20']} {c['erc_20']} {c['near_prot']} {c['eos']} {c['ava']}" for c in networks_before_update)
    networks_list = " ".join(f"{c['any_networks']} {c['bep_20']} {c['trc_20']} {c['erc_20']} {c['near_prot']} {c['eos']} {c['ava']}" for c in networks_after_update)

    update_conditions = {
        'any_networks': 0,
        'bep_20': 1,
        'trc_20': 2,
        'erc_20': 3,
        'near_prot': 4,
        'eos': 5,
        'ava': 6
    }

    update_index = update_conditions.get(callback_query.data, -1)

    if update_index != -1 and int(networks_list_button.split(" ")[update_index]) != int(networks_list.split(" ")[update_index]):
        await callback_query.message.edit_text("Укажите сеть в связке для вывода:", reply_markup=NetworksMenuMarkup().get(networks_list))

def setup_networks(dp) -> None:
    dp.register_callback_query_handler(ask_networks, lambda c: c.data == 'networks')
    dp.register_callback_query_handler(ask_network, lambda c: c.data in ('any_networks', 'bep_20', 'trc_20', 'erc_20', 'near_prot', 'eos', 'ava'))
# CODE EDIT BY T.ME/WHOISSOEE
    # CODE EDIT BY T.ME/WHOISSOEE
        # CODE EDIT BY T.ME/WHOISSOEE
