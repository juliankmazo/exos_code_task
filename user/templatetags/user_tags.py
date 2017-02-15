from django import template
from datetime import date

register = template.Library()


@register.simple_tag
def is_user_allowed(user_birth_date):
    """ Calculate if user is older than 13"""
    if not isinstance(user_birth_date, date):
        return 'Blocked'
    age = (date.today() - user_birth_date).days // 365
    return 'Allowed' if age > 13 else 'Blocked'

@register.simple_tag
def fizz_buzz(random_number):
    """Calculates the fizzbuzz output"""
    if random_number % 3 == 0 and random_number % 5 == 0:
        return 'FizzBuzz'
    elif random_number % 3 == 0:
        return 'Fizz'
    elif random_number % 5 == 0:
        return 'Buzz'
    else:
        return random_number
