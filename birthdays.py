from datetime import datetime, date
from collections import defaultdict

def get_birthdays_per_week(users) :
    birthdays_per_week = defaultdict(list)
    today = datetime.today().date()

    for user in users :
        name = user["name"]
        birthday = user["birthday"].date()
        birthday_this_year = birthday.replace(year=today.year)
        if birthday_this_year < today :
            birthday_this_year = birthday.replace(year=today.year + 1)
        delta_days = (birthday_this_year - today).days
        if delta_days < 7 :
            birthdays_per_week[birthday_this_year.strftime('%A')].append(name)

    print(birthdays_per_week)
