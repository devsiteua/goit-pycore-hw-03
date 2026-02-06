from datetime import datetime

def get_days_from_today(date_str: str) -> int:
    try:
        parsed_date = datetime.strptime(date_str, '%Y-%m-%d').date()
    except ValueError as e:
        raise ValueError("Invalid date format. Please use YYYY-MM-DD") from e

    today = datetime.today().date()
    delta = today - parsed_date
    return delta.days
