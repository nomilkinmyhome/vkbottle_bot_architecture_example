from src.blueprints import user, complex_calculations, simple_keyboard

bps = (
    user.bp,
    complex_calculations.bp,
    simple_keyboard.bp
)

__all__ = ('bps',)
