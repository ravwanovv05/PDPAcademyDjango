from django import template

register = template.Library()


@register.filter(name='length_is')
def length_is(value, length):
    """Check if the length of the value is equal to the given length."""
    return len(value) == length
