from django import template


register=template.Library()

@register.filter(name='rupee')
def rupee(number):
    return "₹ "+str(number)

