from modeltranslation.translator import register, TranslationOptions
from .models import Property

@register(Property)
class PropertyTranslationOptions(TranslationOptions):
    fields = ('title', 'description')
