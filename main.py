import datetime


# Prepare a dict with users who have birthday in the current month

def this_month_birthdays(_lst):
    curr_month = datetime.date.today().month
    
    this_month_birthdays = []

    for user in _lst:
        birthday_time = datetime.datetime.strptime(user['birthday'], "%Y-%m-%d")
        birthday = birthday_time.date()
        
        if birthday.month == curr_month:
            formatted_users = {}
            formatted_users['name'] = user['name']
            formatted_users['birthday'] = birthday.strftime("%Y-%m-%d")
            
            this_month_birthdays.append(formatted_users)
        
    return this_month_birthdays

# Prepare a day and date starting from closest 
def dates_to_be_checked():
    
    today = datetime.datetime.today()
    saturday = today + datetime.timedelta(days=(5 - today.weekday()) % 7)
    friday = saturday + datetime.timedelta(days=6)
    dates = [saturday + datetime.timedelta(days=i) for i in range((friday - saturday).days + 1)]
    date_strings = {d.strftime("%A"): d.strftime("%d") for d in dates}

    return date_strings

def get_birthdays_per_week(list):
    birthdays_this_month = this_month_birthdays(list)
    dates_to_check = dates_to_be_checked()

    birthdays_per_week = { "Monday": [],
        "Tuesday": [],
        "Wednesday": [],
        "Thursday": [],
        "Friday": []
        }

    for day, date in dates_to_check.items():
        # if day in ['Saturday', 'Sunday']:
        #     continue
        birthdays_per_week[day] = []

        for user in birthdays_this_month:
# посмотреть завтра
            if datetime.datetime.strptime(user['birthday'], "%Y-%m-%d").day == int(date):
                if datetime.datetime.strptime(user['birthday'], "%Y-%m-%d").weekday() == 5:
                    birthdays_per_week['Monday'].append(user['name'])
                else:
                    birthdays_per_week[day].append(user['name'])

    for i in birthdays_per_week:
        print(f'{i}: {", ".join(birthdays_per_week[i])}')


if __name__ == "__main__":
    
    users = [
        {'name': 'Богуслава Єрьоменко', 'birthday': '1999-03-06'},
        {'name': 'Ilya', 'birthday': '1999-04-21'},
        {'name': 'Ksenia', 'birthday': '1982-03-18'},
        {'name': 'Nikita', 'birthday': '1982-03-22'},
        {'name': 'Andrey', 'birthday': '1983-03-23'},
        {'name': 'Vlad', 'birthday': '2000-03-23'},
        {'name': 'Misha', 'birthday': '1986-06-10'},
        {'name': 'Roma', 'birthday': '1985-07-21'},
        {'name': 'Arseniy', 'birthday': '1992-03-19'},
        {'name': 'Lesha', 'birthday': '1992-03-29'},
    ]

    get_birthdays_per_week(users)