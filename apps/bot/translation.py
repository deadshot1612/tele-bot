from django.utils import translation
from django.utils.translation import gettext_lazy as _


def get_translation(string, locale):
    translation.activate(locale)
    val = _(string)
    translation.deactivate()
    return val