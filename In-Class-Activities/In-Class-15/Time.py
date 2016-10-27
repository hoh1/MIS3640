class Time:
    """Represents the time of day.
    attributes: hour, minute, second
    """

time = Time()
time.hour = 1
time.minute = 50
time.second = 30

print(time.hour, time.minute, time.second)  #original time (1:50:30)

later = Time()
later.hour = time.hour
later.minute = time.minute + 5
later.second = time.second

print(later.hour, later.minute, later.second)   #later time (1:55:30)

""""""""""""""""""""""""""""""""""""
# Exercise 1
""""""""""""""""""""""""""""""""""""


def print_time(t):
    """Prints a string representation of the time.
    t: Time object
    """
    print('%.2d:%.2d:%.2d' % (t.hour, t.minute, t.second))

print_time(time)  #print the times with better format
print_time(later)

def is_after(t1, t2):
    """Returns True if t1 is after t2; false otherwise.
    Challenge: NO IF STATEMENT!
    """
    return (t1.hour, t1.minute, t1.second) > (t2.hour, t2.minute, t2.second)


print(is_after(time, later))    


""""""""""""""""""""""""""""""""""""
# Prototyping
""""""""""""""""""""""""""""""""""""


def add_time(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    TO-DO: improve this function
    """
    sum = Time()
    sum.hour = t1.hour + t2.hour
    sum.minute = t1.minute + t2.minute
    sum.second = t1.second + t2.second
    
    if sum.second >= 60:   #set conditionals to make a legit time
        sum.second -= 60
        sum.minute += 1

    if sum.minute >= 60:
        sum.minute -= 60
        sum.hour += 1

    return sum

# Uncomment below for testing

start = Time()
start.hour = 9
start.minute = 45
start.second =  30

duration = Time()
duration.hour = 1
duration.minute = 35
duration.second = 45

done = add_time(start, duration)
print_time(done)


""""""""""""""""""""""""""""""""""""
# Designed Development
""""""""""""""""""""""""""""""""""""


def int_to_time(seconds):
    """Makes a new Time object.
    seconds: int seconds since midnight.
    """
    time = Time()
    minutes, time.second = divmod(seconds, 60)
    time.hour, time.minute = divmod(minutes, 60)
    return time


def time_to_int(time):
    """Computes the number of seconds since midnight.
    time: Time object.
    """
    minutes = time.hour * 60 + time.minute
    seconds = minutes * 60 + time.second
    return seconds


def add_time2(t1, t2):
    """Adds two time objects.
    t1, t2: Time
    returns: Time
    """
    assert valid_time(t1) and valid_time(t2)
    seconds = time_to_int(t1) + time_to_int(t2)
    return int_to_time(seconds)

done = add_time2(start, duration)
print_time(done)

def valid_time(time):
    """Checks whether a Time object satisfies the invariants.
    time: Time
    returns: boolean
    """
    if time.hour < 0 or time.minute < 0 or time.second < 0:
        return False
    if time.minute >= 60 or time.second >= 60:
        return False
    return True


""""""""""""""""""""""""""""""""""""
# Exercise 3
""""""""""""""""""""""""""""""""""""


def substract_time(t1, t2):
    """Substracts two time objects.
    t1, t2: Time
    returns: Time
    """
    seconds = time_to_int(t1) - time_to_int(t2)
    return int_to_time(abs(seconds))

print_time(substract_time(done, duration))
print_time(substract_time(time, later))

""""""""""""""""""""""""""""""""""""
# Exercise 4
""""""""""""""""""""""""""""""""""""


def mul_time(t1, factor):
    """Multiplies a Time object by a factor."""
    seconds = time_to_int(t1) * factor
    return int_to_time(abs(seconds))

print_time(time)
print('after multiplied by 5:', end=' ')
print_time(mul_time(time, 5))


def main():
    # if a movie starts at noon...
    noon_time = Time()
    noon_time.hour = 12
    noon_time.minute = 0
    noon_time.second = 0

    print('Starts at', end=' ')
    print_time(noon_time)

    # and the run time of the movie is 109 minutes...
    movie_minutes = 109
    run_time = int_to_time(movie_minutes * 60)
    print('Run time', end=' ')
    print_time(run_time)

    # what time does the movie end?
    end_time = add_time2(noon_time, run_time)
    print('Ends at', end=' ')
    print_time(end_time)


# if __name__ == '__main__':
#     main()