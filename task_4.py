from datetime import datetime, timedelta

DAYS_AHEAD = 6
SATURDAY_WEEKDAY = 5
SUNDAY_WEEKDAY = 6
DAYS_TO_MONDAY_FROM_SATURDAY = 2
DAYS_TO_MONDAY_FROM_SUNDAY = 1

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        birthday_this_year = birthday_date.replace(year=today.year)
        
        if birthday_this_year < today:
            birthday_this_year = birthday_this_year.replace(year=today.year + 1)
        
        days_diff = (birthday_this_year - today).days
        
        if 0 <= days_diff <= DAYS_AHEAD:
            congratulation_date = birthday_this_year
            
            if congratulation_date.weekday() == SATURDAY_WEEKDAY:
                congratulation_date += timedelta(days=DAYS_TO_MONDAY_FROM_SATURDAY)
            elif congratulation_date.weekday() == SUNDAY_WEEKDAY:
                congratulation_date += timedelta(days=DAYS_TO_MONDAY_FROM_SUNDAY)
            
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
    
    return upcoming_birthdays