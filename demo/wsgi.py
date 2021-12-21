import os
import logging
import sys

from telebot import TeleBot
from django.core.wsgi import get_wsgi_application
from django.conf import settings
from telebot.apihelper import ApiTelegramException
from threading import Thread

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'demo.settings')

def initialize_app():
    bot = TeleBot(token=settings.BOT_TOKEN)
    try:
        bot.set_webhook(f'{settings.SERVER_ADDRESS}/{settings.BOT_TOKEN}/')
    except ApiTelegramException:
        logger = logging.getLogger('telegram')
        logger.error(
            'ApiTelegramException',
            exc_info=sys.exc_info(),
            extra=dict(status_code=500,
            request=None
            )
        )
    return get_wsgi_application()

application = initialize_app()
