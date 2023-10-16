from django.template.defaulttags import register


@register.filter
def str_to_range(obj):
    try:
        return range(int(obj))
    except:
        return ''
