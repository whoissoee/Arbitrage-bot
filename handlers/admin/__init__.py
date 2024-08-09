from .admin_menu import setup_admin_menu
from .check_users import setup_check_users
from .free_work import setup_free_work
from .broadcast import setup_broadcast
from .get_users_file import setup_get_users_file
from .get_users_pay_file import setup_get_users_pay_file
from .update_start_message import setup_update_message

def setup_admin(dp) -> None:
    setup_broadcast(dp)
    setup_admin_menu(dp)
    setup_check_users(dp)
    setup_free_work(dp)
    setup_get_users_file(dp)
    setup_get_users_pay_file(dp)
    setup_update_message(dp)
