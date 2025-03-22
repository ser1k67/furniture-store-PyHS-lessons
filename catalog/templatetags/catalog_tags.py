from django import template
from django.utils.http import urlencode

from catalog.models import Categories

register = template.Library()

# что бы категорий отображались во всех страницах
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()

# добавляет к существующим параметрам новые параметры запроса
@register.simple_tag(takes_context=True)
def change_params(context, **kwargs):
    query = context['request'].GET.dict()
    query.update(kwargs)
    return urlencode(query)
