from django import template

register = template.Library()

@register.filter(name='censor')
def censor(value):
    return value.replace('нежелательное', '*')
