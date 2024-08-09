from utils import ReplyMarkupConstructor

class AdminMenuMarkup(ReplyMarkupConstructor):
    check_users = "📈 Посмотреть кол-во пользователей в бд"
    two_hours_work = "🧑‍💻 Выдать пробный период пользователю (2 часа)"
    change = "🆕 Изменить приветствие"
    broadcast = "📣 Рассылка"
    get_users_file = "📩 Выгрузить пользователей в файл"
    get_users_pay_file = "📩 Выгрузить пользователей c доступом в файл"

    def get(self):
        actions = [
            {"text": self.check_users},
            {"text": self.two_hours_work},
            {"text": self.change},
            {"text": self.broadcast},
            {"text": self.get_users_file},
            {"text": self.get_users_pay_file}
        ]
        schema = [2, 2, 2]
        return self.markup(actions, schema, resize_keyboard=True)

class AdminCancelMarkup(ReplyMarkupConstructor):
    cancel_btn = "❌ Отменить"

    def get(self):
        return self.markup([{"text": self.cancel_btn}], [1], resize_keyboard=True)

class MainMenuMarkup(ReplyMarkupConstructor):
    bundles_btn = "💼 Получить связки"
    settings_btn = "⚙️ Настройки"

    def get(self):
        actions = [
            {"text": self.bundles_btn},
            {"text": self.settings_btn}
        ]
        schema = [1, 1]
        return self.markup(actions, schema, resize_keyboard=True)

