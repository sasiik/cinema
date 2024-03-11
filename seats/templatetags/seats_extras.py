from django import template

register = template.Library()

# Custom concatenator for Jinja 

@register.filter
def addstr(arg1, arg2):
    # Concatenating two strings
    return str(arg1) + str(arg2)