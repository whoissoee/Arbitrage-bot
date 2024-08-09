from aiogram.dispatcher.filters.state import StatesGroup, State


class AdminStates(StatesGroup):

    WAIT_BROADCAST_MESSAGE = State()
    WAIT_USER_ID_MESSAGE = State()
    WAIT_UPDATE_MSG = State()
    WAIT_UPDATE_MSG2 = State()