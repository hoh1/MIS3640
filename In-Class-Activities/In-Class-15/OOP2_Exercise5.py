import datetime
  
class Time:
     """Represents the time of day.
        
     attributes: hour, minute, second
     """
 
def __init__(self, hour=0, minute=0, second=0):
    """Initializes a time object.
    hour: int
    minute: int
    second: int or float
    """
    self.hour = hour
    self.minute = minute
    self.second = second
 
def print_time(self):
    """Returns a string representation of the time."""
    print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))
 
def time_to_int(self):
    """Returns the total number of seconds past midnight of a Time object."""
    minutes = self.hour * 60 + self.minute
    seconds = minutes * 60 + self.second
    return seconds
 
def is_after(t1, t2):
    """Returns a boolean True if Time object t1 follows Time object t2 chronologically."""
    return t1.time_to_int() > t2.time_to_int()
 
def add_time(self, other):
    """Returns a Time object equal to the addition of two Time objects"""
    final = self.time_to_int() + other.time_to_int()
    timey = int_to_time(final)
    return timey
 
def subtract_time(self, other):
    """Returns a Time object equal to the amount of time between two Time objects"""
    final = abs(self.time_to_int() - other.time_to_int())
    timey = int_to_time(final)
    return timey
 
def mul_time(self, other):
    """Returns a Time object equal to the product of a Time object and a number"""
    final = self.time_to_int() * other
    timey = int_to_time(final)
    return timey
 
def race_speed(finish, distance):
    """Returns mile time as a Time object when given a finish time and number of miles run."""
    return finish.mul_time(1/distance)
 
 
def int_to_time(seconds):
    """Creates a Time object from a total number of seconds past midnight."""
    minutes = seconds // 60
    second = seconds % 60
    hour = minutes // 60
    minute = minutes % 60
    my_time = Time(hour, minute, second)
    return my_time
 
 
def print_day():
    """Prints the current day of the week in human-readable format"""
    my_date = datetime.datetime.now()
    print('The current day of the week is {0:%A}'.format(my_date, 'weekday'))
 
 
def birthday_printer(date):
    """Takes a birthdate as datetime and prints the user's age as well as the time until their next birthday"""
    now = datetime.datetime.today()
    age_delta = now - date
    age = age_delta.days // 365
    next_bday = datetime.datetime(now.year, date.month, date.day)
    time_til = next_bday - now
    if time_til.total_seconds() < 0:
        next_bday = datetime.datetime(now.year + 1, date.month, date.day)
        time_til = next_bday - now
    minutes, second = divmod(time_til.seconds, 60)
    hour, minute = divmod(minutes, 60)
    print('You are currently %d years old' %(age))
    print('There are %d days, %d hours, %d minutes, and %d seconds until your birthday' %(time_til.days, hour, minute, second))
     
 
def doubleday(d1, d2):
    """Takes two birthdates and prints the first person is 2 times older than the second person"""
    dif = abs(d1 - d2)
    if d1 > d2:
        dd = d1 + dif
    elif d2 > d1:
        dd = d2 + dif
    else:
        print('These are the same date!')
    print('Your Double Day is %s' %(dd))
 
 
def main():
    start = Time(1, 31, 2)
 
    later = Time(1, 32, 5)
  
    Time.print_time(start.add_time(later))
    Time.print_time(start.subtract_time(later))
    Time.print_time(race_speed(start, 8))
 
    print_day()
    my_birthday = datetime.datetime(1992, 2, 26)
    my_birthdate = datetime.date(1992, 2, 26)
    your_birthdate = datetime.date(2005, 1, 5)
    birthday_printer(my_birthday)
    doubleday(your_birthdate, my_birthdate)
 
 
if __name__ == '__main__':
    main() 