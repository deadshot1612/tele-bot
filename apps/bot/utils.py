from django.utils import translation
from contextlib import contextmanager

from apps.bot.models import BotUser


@contextmanager
def change_locale(locale):
    resource = translation.activate(locale)
    try:
        yield resource
    finally:
        translation.deactivate()


def with_locale(func):
    def wrapper(message, *args, **kwargs):
        user = BotUser.objects.filter(id=message.from_user.id).first()
        locale = user.locale if user else BotUser.Locale.RU
        with change_locale(locale):
            func(message, *args, **kwargs)
    return wrapper
