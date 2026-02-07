from datetime import datetime, timedelta

def get_upcoming_birthdays(users: list[dict[str, str]]) -> list[dict[str, str]]:
    result = []
    today = datetime.today().date()

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()

        birthday_this_year = birthday_date.replace(year=today.year)

        if birthday_this_year < today:
            next_birthday = birthday_this_year.replace(year=today.year + 1)
        else:
            next_birthday = birthday_this_year

        delta_days = (next_birthday - today).days

        if not (0 <= delta_days <= 7):
            continue

        day_week = next_birthday.weekday()
        if day_week == 5:
            congratulation_date = next_birthday + timedelta(days=2)
        elif day_week == 6:
            congratulation_date = next_birthday + timedelta(days=1)
        else:
            congratulation_date = next_birthday

        result.append({
            "name": user["name"],
            "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
        })

    return result
