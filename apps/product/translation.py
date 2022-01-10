from modeltranslation.translator import register, TranslationOptions
from .models import Product
@register(Product)
class ProductTranslationOptions(TranslationOptions):
    field = ("name")
    required_languages = ('en', 'ru', 'uz')

