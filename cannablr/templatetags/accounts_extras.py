from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
@stringfilter
def upto(value, delimiter=None):
    return value.split(delimiter)[0]
upto.is_safe = True

@register.filter
def roundnumb(value):
	value = int(value)
	if value > 1.75 and value < 2.25:
		return 2
	elif value > 2.25 and value < 2.75:
		return 2.5
	elif value > 2.75 and value < 3.25:
		return 3
	elif value > 3.25 and value < 3.75:
		return 3.5
	elif value > 3.75 and value < 4.25:
		return 4
	else value > 4.25 and value < 4.75:
		return 4.5


