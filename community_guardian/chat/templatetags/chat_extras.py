import re
from django import template
from django.utils.safestring import mark_safe

register = template.Library()

@register.filter
def urlize_message(value):
    url_pattern = re.compile(r'(https?://[^\s]+)')
    return mark_safe(url_pattern.sub(r'<a href="\1" target="_blank" class="text-blue-600 underline">\1</a>', value))