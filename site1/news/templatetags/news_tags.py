from django import template
from news.models import Category

register = template.Library()

@register.simple_tag() # декоратор
def get_categories():
    return Category.objects.all()
