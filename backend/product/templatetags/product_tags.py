from django import template

register = template.Library()


@register.filter(name='delta')
def delta(value, arg):
    'Разность двух значений'
    return value - arg





