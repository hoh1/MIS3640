class Time():
    """
    Represents the time of day.

    attributes: hour, minute, second
    """
    def __init__(self, hour, minute, second):
        self.hour = hour
        self.minute = minute
        self.second = second
    
    def print_time(self):
        """Prints a string represenation of the time."""
        print('%.2d:%.2d:%.2d' % (self.hour, self.minute, self.second))

    def time_to_int(self):
        minutes = self.hour * 60 + self.minute
        seconds = minutes * 60 + self.second
        return seconds

    def is_after(self, other):
        return self.time_to_int() > other.time_to_int()

    def is_as_expected(self, duration, arrival):
        return self.time_to_int() + duration.time_to_int() == arrival.time_to_int() 

    def increment(self, seconds):
        seconds += self.time_to_int()
        return int_to_time(seconds)
        
def int_to_time(seconds):
    '''
    Makes a new time object
    Seconds: 
    '''
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes, 60)
    return time

# def print_time(t):
#     print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

start = Time(9, 45, 0)
# start.hour = 9
# start.minute = 45
# start.second = 0
# print_time(start)   # printing using the def print_time outside class time()

#below is a OOP start printing method
start.print_time()    # using def print_time inside class Time(); here 'start' is an object. declare a command to an object;
print(start.time_to_int())

end = start.increment(2000)
end.print_time()
print(end.is_after(start))

traffic = Time(0, 30, 0)
# traffic.hour = 0
# traffic.minute = 30
# traffic.second = 0

expected_time = Time(10, 15, 0)
# expected_time.hour = 10
# expected_time.minute = 15
# expected_time.second = 0

# traffic.print_time()
# expected_time.print_time()
# print(start.is_as_expected(traffic, expected_time))

