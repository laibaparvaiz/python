import calendar

class MyCalendar(calendar.Calendar):
    def count_weekday_in_year(self, year, weekday):
        count = 0
        for month  in range(1,13):
            for week in self.monthdays2calendar(year, month):
                for day,  day_of_week in week:
                    if day != 0 and day_of_week == weekday:
                        count += 1 
        return count
    
cal = MyCalendar()
print(cal.count_weekday_in_year(2019, 0))