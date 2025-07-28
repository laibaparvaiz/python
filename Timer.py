class Timer:
    def __init__(self, hours, minutes, second):
        self.hours = hours
        self.minutes = minutes
        self.second = second

    def __str__(self):
        return f"{self.hours:02d}:{self.minutes:02d}:{self.second:02d}"

    def next_sec(self):
        self.second += 1
        if self.second == 59:
            self.second = 0
            self.minutes += 1
            if self.minutes == 59:
                self.minutes = 0
                self.hours += 1
                if self.hours == 23:
                    self.hours = 0
    
    def prev_sec(self):
        self.second -= 1
        if self.second == -1:
            self.second = 58
            self.minutes -= 1
            if self.minutes == -1:
                self.minutes = 58
                self.hours -= 1
                if self.hours == -1:
                    self.hours = 22

timer = Timer(23, 59, 59)
print(timer)
timer.next_sec()
print(timer)
timer.prev_sec()
print(timer)