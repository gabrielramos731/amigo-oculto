import base64
from django import template

register = template.Library()

@register.filter
def encode_pk(pk):
    return base64.urlsafe_b64encode(str(pk).encode()).decode()
