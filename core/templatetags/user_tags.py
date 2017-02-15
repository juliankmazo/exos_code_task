from datetime import date
from django import template

register = template.Library()


@register.simple_tag
def is_user_allowed(user_birth_date):
    """ Calculate if user is older than 13"""
    if not isinstance(user_birth_date, date):
        return 'Blocked'
    age = (date.today() - user_birth_date).days // 365
    return 'Allowed' if age > 13 else 'Blocked'


@register.simple_tag
def bizz_fuzz(random_number):
    """Calculate the fizzbuzz output"""
    if random_number % 3 == 0 and random_number % 5 == 0:
        return 'BizzFuzz'
    elif random_number % 3 == 0:
        return 'Bizz'
    elif random_number % 5 == 0:
        return 'Fuzz'
    else:
        return random_number
