import random

ROSTER = {"Beshansky": 0,
          "Collins": 0,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 0,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 0,
          "Wolf": 0}


def call(roster):
    """
    Among the names that are called least times,
    return one name randomly

    roster: a dict of names and integers
    
    TO-DO: update dict after every call
    TO-DO: write it back to CSV file
    """
    value_list = roster.values() #define value_list, which is 'all' the values in ROSTER
    min_value = min(value_list) #define min_value, which is the 'minimum' values in value_list
    
    names = []  #temporary list to store the minimum values
    for name, number in roster.items(): #here, key = name, value = number
        if number == min_value:
            names.append(name)
    return random.choice(names)
    
print(call(ROSTER))