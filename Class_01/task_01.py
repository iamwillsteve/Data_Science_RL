class Clock:
    def __init__(self, hour, minute, second):
        self.__verify_input(hour, minute, second)
        self.hour = hour
        self.minute = minute
        self.second = second
        self.time = (hour, minute, second)

    def __verify_input(self, hour, minute, second):
        if hour < 0 or hour >= 24:
            raise ValueError('El valor de hora debe estar entre 0 y 23')
        if minute < 0 or minute >= 60:
            raise ValueError('El valor de minuto debe estar entre 0 y 59')
        if second < 0 or second >= 60:
            raise ValueError('El valor de segundo debe estar entre 0 y 59')
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
        return f'{self.hour:02d}:{self.minute:02d}:{self.second:02d}'

class Calendar:
    def __init__(self, day, month, year):
        self.__verify_day_input(day, month, year)
        self.day = day
        self.month = month
        self.year = year
        self.date = (day, month, year)

    def __verify_day_input(self, day, month, year):
        if day < 0 or day > 31:
            raise ValueError('El valor de día debe estar entre 0 y 31')
        if month < 0 or month > 12:
            raise ValueError('El valor del mes debe estar entre 1 y 12')
        if year < 0 or year > 9999:
            raise ValueError('El valor de año debe estar entre 0 y 9999')
        if (month == 4 or month == 6 or month == 9 or month == 11) and day > 30:
            raise ValueError('El mes ingresado no tiene más de 30 días en el calendario')
        if month == 2 and self.__is_leap(year) and day > 29:
            raise ValueError('Febrero no tiene más de 29 días en el calendario en año bisiesto')
        if month == 2 and not self.__is_leap(year) and day > 28:
            raise ValueError('Febrero no tiene más de 28 días en el calendario en año no bisiesto')

    def __is_leap(self, year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
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
            if self.__is_leap(self.year):
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
        return f'{self.day:02d}/{self.month:02d}/{self.year:04d}'

class CalendarClock(Calendar, Clock):
    def __init__(self, day, month, year, hour, minute, second):
        Calendar.__init__(self, day, month, year)
        Clock.__init__(self, hour, minute, second)

    def tick(self):
        Clock.tick(self)
        if self.second == 0 and self.minute == 0 and self.hour == 0:
            Calendar.advance(self)

    def __str__(self):
        return f'Date: {self.day:02d}/{self.month:02d}/{self.year:04d} \nHour: {self.hour:02d}:{self.minute:02d}:{self.second:02d} \n'

calendario = CalendarClock(29, 2, 2024, 23, 59, 59)
print(calendario)
calendario.tick()
print(calendario)
