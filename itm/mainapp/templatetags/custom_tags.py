from django.template.defaulttags import register
from datetime import datetime as dt


@register.filter
def str_to_range(obj):
    try:
        return range(int(obj))
    except:
        return ''


@register.filter
def str_date(obj):
    return obj.strftime('%d.%m.%Y в %H:%M:%S')
