from django import template

from catalog.models import Categories

register = template.Library()

# что бы категорий отображались во всех страницах
@register.simple_tag()
def tag_categories():
    return Categories.objects.all()
