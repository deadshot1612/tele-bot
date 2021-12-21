from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from telebot import types

from apps.bot import bot
from apps.bot.utils import change_locale, with_locale
from apps.bot.models import BotUser
from apps.bot import messaging

# Create your views here.


@csrf_exempt
def handle(request):
    request_body_dict = request.body.decode('UTF-8')
    update = types.Update.de_json(request_body_dict)
    bot.process_new_updates([update])
    return HttpResponse(200)


@bot.message_handler(commands=['start'])
@with_locale
def on_start(message: types.Message):
    user_id = message.from_user.id
    if BotUser.objects.filter(id=user_id).exists():
        messaging.send_hello(message)
    else:
        messaging.request_language(message)
        bot.register_next_step_handler(message, on_language_specified)


@bot.message_handler(content_types=['text'])
@with_locale
def on_language_specified(message):
    locale = BotUser.Locale.get_from_value(message.text)
    BotUser.objects.update_or_create(id=message.from_user.id, locale=locale)
    with change_locale(locale):
        messaging.request_full_name(message)
        bot.register_next_step_handler(message, on_full_name_specified)


@bot.message_handler(content_types=['text'])
@with_locale
def on_full_name_specified(message):
    
    full_name= str(message.text)
    BotUser.objects.update_or_create(id=message.from_user.id, full_name = full_name)
    messaging.request_number(message)
    bot.register_next_step_handler(message, on_number_specified)


@bot.message_handler(content_types=['text'])
@with_locale
def on_number_specified(message):
    pass