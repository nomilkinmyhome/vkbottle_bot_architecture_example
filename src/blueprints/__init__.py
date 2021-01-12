from src.blueprints.user import info_handler
from src.blueprints.complex_calculations import calculation_handler

bps = (
    info_handler,
    calculation_handler,
)

__all__ = ('bps',)
