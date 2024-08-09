from .exchanges import setup_exchanges
from .getbundles import setup_bundles
from .networks import setup_networks
from .order_size import setup_order_size
from .pay import setup_pay
from .sittings import setup_sittings
from .spread import setup_spread
from .start import setup_start

def setup_private(dp) -> None:
    setup_start(dp) # TODO: Можно переписать фильтр, в целом рабоает корректно
    setup_exchanges(dp)
    setup_networks(dp)
    setup_order_size(dp)
    setup_pay(dp)
    setup_sittings(dp)
    setup_spread(dp) # TODO: Доделать кнопки, не работают + листают в одну сторону
    setup_bundles(dp) # TODO: Ускорить код (корутины не работают, добавь воркеров + оповещение для пользователя что нужно подождать) 