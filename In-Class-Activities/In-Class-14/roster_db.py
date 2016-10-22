import dbm
import random

ROSTER = {"Beshansky": 0,
          "Collins": 1,
          "Fischer": 1,
          "Giovanucci": 0,
          "Jain": 0,
          "Kim": 0,
          "Lauture": 0,
          "Lee": 0,
          "Maddox": 0,
          "Martinez": 0,
          "Mendez": 0,
          "Oh": 1,
          "Petrone": 1,
          "Posada": 0,
          "Rule": 1,
          "Schilb": 0,
          "Tariq": 0,
          "Wang": 1,
          "Wolf": 0}


def create_db(db_name, roster=ROSTER):
    '''
    return a new dabase containing names and 0s
    
    roster: a dictionary of names and number of visits
    '''
    db = dbm.open(db_name, 'c')
    for student, visits in roster.items():
        db[student] = str(visits)                #why assign the value as string?
    db.close()
    return db


def call(db_name):       #note, the for loop below is based on 'db'; while 'lists' are used for sorting out(append);
    '''
    Among the names that are called least times,
    return one name randomly. Update database after each call.
    db_name: the name of database
    
    returns one name
    '''
    db = dbm.open(db_name, 'c')

    visits_list = []            #get the 'visit' value for every student and store it in visits_list;
    for student in db:
        visits_list.append(int(db[student]))

    min_visits = min(visits_list)         #there, find the ones w/ min values

    names = []                             #appends only those with min_vists in names;
    for student in db:
        if int(db[student]) == min_visits:
            names.append(student)

    name_to_update = random.choice(names)   #update randomly ONLY from the list 'names', the ones w/ min_visits;
    db[name_to_update] = str(min_visits + 1)  # add 1 to min_visits
    return name_to_update


def display_all(db_name):
    '''
    display all names and values
    db_name: the name of database
    '''
    db = dbm.open(db_name, 'r')
    for student in db:
        print(student, int(db[student]))
    db.close()


def main():
    new_db = create_db('db_student')

    display_all('db_student')
    for i in range(3):
        print(call('db_student'))


if __name__ == '__main__':
    main()