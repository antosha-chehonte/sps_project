from django import template
from catalog.views import DocType

register = template.Library()


@register.simple_tag(name='get_list_doc_types')
def get_doc_types():
    return DocType.objects.all()
