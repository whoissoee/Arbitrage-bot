from aiogram.dispatcher.filters.state import StatesGroup, State

class ParseState(StatesGroup):
    ListBundles = State()
    PageNumber = State()