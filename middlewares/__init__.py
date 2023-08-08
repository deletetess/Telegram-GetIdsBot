
from aiogram import Dispatcher

from .throttling import ThrottlingMiddleware


__all__ = [
    "ThrottlingMiddleware",
    "setup"
]


def setup(dp: Dispatcher) -> None:
    for mid in [
        ThrottlingMiddleware()
    ]:
        dp.message.middleware(mid)
