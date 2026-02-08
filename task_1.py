from datetime import datetime, date as date_class

def get_days_from_today(date: str) -> int:
    input_date = datetime.strptime(date, "%Y-%m-%d").date()
    today = date_class.today()
    return (today - input_date).days

user_date = input("Введіть дату у форматі YYYY-MM-DD: ")

try:
    result = get_days_from_today(user_date)
    print("Кількість днів між введеною датою та сьогодні:", result)
except ValueError:
    print("Помилка! Будь ласка, введіть дату у форматі YYYY-MM-DD.")

