from django import template
import datetime
import locale

register = template.Library()

@register.simple_tag
def addDays(days, format):
   print(locale.getlocale(locale.LC_TIME))
   newDate = datetime.date.today() + datetime.timedelta(days=days)
   return newDate.strftime(format)