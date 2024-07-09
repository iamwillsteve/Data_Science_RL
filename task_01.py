class Clock:
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = (hour, minute, second)

    def tick(self):
        self.second += 1
        if self.second == 60:
            self.second = 0
            self.minute += 1
        if self.minute == 60:
            self.minute = 0
            self.hour += 1
        if self.hour == 24:
            self.hour = 0
        return self.second

    def __str__(self):
        return (f'{self.hour}:{self.minute}:{self.second}')

class Calendar:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year
        self.date = (day, month, year)

    def __is_leap(self):
        if self.year % 4 == 0:
            if self.year % 100 == 0:
                if self.year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    def advance(self):
        self.day += 1
        if self.month == 2:
            if self.__is_leap():
                if self.day == 30:
                    self.day = 1
                    self.month += 1
            else:
                if self.day == 29:
                    self.day = 1
                    self.month += 1

        if self.month == 4 or self.month == 6 or self.month == 9 or self.month == 11:
            if self.day == 31:
                self.day = 1
                self.month += 1

        if self.day == 32:
            self.day = 1
            self.month += 1
        if self.month == 13:
            self.month = 1
            self.year += 1

        return self.day

    def __str__(self):
        return (f'{self.day}/{self.month}/{self.year}')

class CalendarClock(Calendar, Clock):
    def __init__(self, day, month, year, hour, minute, second):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hour, minute, second)

    def tick(self):
        Clock.tick(self)
        if self.second == 0 and self.minute == 0 and self.hour == 0:
            Calendar.advance(self)

    def __str__(self):
        return f'Date: {self.day}/{self.month}/{self.year} \nHour: {self.hour}:{self.minute}:{self.second} \n'

calendario = CalendarClock(29, 2, 2024, 23, 59, 59)
print(calendario)
calendario.tick()
print(calendario)
