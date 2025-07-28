class weekdayerror(Exception):
    pass

class weeker:
    __days = ['mon', 'tue', 'wed', 'thu', 'fri', 'satur', 'sun']
    def __init__(self, day):
        if day not in weeker.__days:
           raise weekdayerror
        self.__current_days_index = weeker.__days.index(day)

    def __str__(self):
        return weeker.__days[self.__current_days_index]
    
    def add_days(self, n):
        self.__current_days_index = (self.__current_days_index + n) % 7

    def subtract_days(self, n):
        self.__current_days_index = (self.__current_days_index - n) % 7

try:
    weekday = weeker('mon')          
    print(weekday)                   
    weekday.add_days(15)
    print(weekday)                   
    weekday.subtract_days(23)
    print(weekday)                   
    weekday = weeker('Monday')       
except weekdayerror:
    print("Sorry, I can't serve your request.")
