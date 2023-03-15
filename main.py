import datetime
from random import randint
import calendar

# Generating random birthdays for list 
def get_random_birthday():
    year = randint(1980, 2000)
    month = randint(1, 12)
    days_in_month = calendar.monthrange(year, month)[1]
    random_day = randint(1, days_in_month)
    date = datetime.date(year, month, random_day)
    return date

# list of random users

users = [
    {'name': 'Slavik', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Ilya', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Ksenia', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Nikita', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Andrey', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Vlad', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Misha', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Roma', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Arseniy', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
    {'name': 'Lesha', 'birthday': get_random_birthday().strftime("%Y-%m-%d")},
]


def get_birthdays_per_week(users):
    today_day = datetime.date.today().day
    today_month = datetime.date.today().month
    for user in users:
        birthday_time = datetime.datetime.strptime(user['birthday'], "%Y-%m-%d")
        birthday = birthday_time.date()
        print(birthday)



   

get_birthdays_per_week(users)

