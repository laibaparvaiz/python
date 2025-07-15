def is_year_leap(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def days_in_month(year, month):
    if month < 1 or month > 12:
        return None
    days = [31, 29 if is_year_leap(year) else 28, 31, 30, 31, 30,
            31, 31, 30, 31, 30, 31]
    return days[month - 1]

def day_of_year(year, month, day):
    if month < 1 or month > 12:
        return None
    if day < 1 or day > days_in_month(year, month):
        return None

    total_days = 0
    for m in range(1, month):
        total_days += days_in_month(year, m)
    total_days += day
    return total_days

print(day_of_year(2000, 12, 31))  
