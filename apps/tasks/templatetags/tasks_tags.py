from django import template
from datetime import datetime, timedelta, date
from time import timezone
from django.conf import settings
from django.template.defaultfilters import date
from django.utils import timezone

register = template.Library()


@register.simple_tag
def addDays(days, format):
    tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
    formatted = date(datetime.now(tz=tzinfo) + timedelta(days=days), format)
    return formatted
