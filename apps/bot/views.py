from django.http.response import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.translation import gettext_lazy as _
from telebot import types

from apps.bot import bot
from apps.bot.utils import change_locale, with_locale
from apps.bot.models import BotUser
from apps.bot import messaging


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
        bot.register_next_step_handler(message, on_command_specified)
    else:
        messaging.request_language(message)
        bot.register_next_step_handler(message, on_language_specified)



@with_locale
def on_language_specified(message):
    locale = BotUser.Locale.get_from_value(message.text)
    BotUser.objects.update_or_create(id=message.from_user.id, locale=locale)
    with change_locale(locale):
        messaging.request_full_name(message)
        bot.register_next_step_handler(message, on_full_name_specified)



@with_locale
def on_full_name_specified(message):
    
    full_name= str(message.text)
    BotUser.objects.update(id=message.from_user.id, full_name = full_name)
    messaging.request_number(message)
    bot.register_next_step_handler(message, on_number_specified)



@with_locale
def on_number_specified(message):
    if message.contact is not None:
        phone_number = message.contact.phone_number
    else:
        phone_number = message.text
    BotUser.objects.update(id=message.from_user.id, phone_number = phone_number)
    messaging.congrat(message)
    bot.register_next_step_handler(message, on_command_specified)


@with_locale
def on_command_specified(message: types.Message):
    if message.text == str(_("Settings")):
        messaging.settings(message)
        bot.register_next_step_handler(message, on_changes_specified)
    if message.text ==str(_("Add ad")):
        messaging.add_ad(message)



@with_locale
def on_changes_specified(message: types.Message):
    if message.text == str(_("Change language")):
        messaging.request_language(message)
        bot.register_next_step_handler(message, on_language_change_specified)
    elif message.text == str(_("Change Name")):
        messaging.change_name(message)
        bot.register_next_step_handler(message, on_name_change_specified)
    elif message.text == str(_("Change Phone Number")):
        messaging.change_number(message)
        bot.register_next_step_handler(message, on_number_change_specified)
    elif message.text == str(_("Back")):
        messaging.back(message)
        bot.register_next_step_handler(message, on_command_specified)


@with_locale
def on_name_change_specified(message: types.Message):
    if message.text == str(_("Back")):
        messaging.back(message)
        bot.register_next_step_handler(message, on_command_specified)
    else:
        full_name = str(message.text)
        BotUser.objects.update(id=message.from_user.id, full_name = full_name)
        messaging.send_new_status(message)
        bot.register_next_step_handler(message, on_changes_specified)


@with_locale
def on_language_change_specified(message: types.Message):
        locale = BotUser.Locale.get_from_value(message.text)
        BotUser.objects.update(id=message.from_user.id, locale = locale)
        messaging.send_new_status(message)
        bot.register_next_step_handler(message, on_changes_specified)

@with_locale
def on_number_change_specified(message):
    if message.text == str(_("Back")):
        messaging.back(message)
        bot.register_next_step_handler(message, on_command_specified)
    else:
        if message.contact is not None:
            phone_number = message.contact.phone_number
        else:
            phone_number = message.text
        BotUser.objects.update(id=message.from_user.id, phone_number = phone_number)
        messaging.send_new_status(message)
        bot.register_next_step_handler(message, on_changes_specified)