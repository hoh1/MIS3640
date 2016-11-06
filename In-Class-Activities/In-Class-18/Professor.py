from BabsonPerson import BabsonPerson
from Person import Person
from Student import Student

class Professor(BabsonPerson):
    def __init__(self, name, department):
        BabsonPerson.__init__(self, name)
        self.dept = department    

    def getDept(self):
        return self.dept

    def speak(self, utterance):
        return BabsonPerson.speak(self, " As a professor, " + utterance)  


def isProfessor(obj):
    return isinstance(obj, Professor)     


def main():
    s1 = Professor('Shankar', 'IT Dept')
    s2 = Professor('Zhi Li', 'IT Dept')
    s3 = Professor('Bret Breo', 'MOB Dept')
    s4 = Student('Mark Oh')

    professorList = [s1, s2, s3, s4]

    print(s1)

    print(s1.getDept())

    print(s1.speak('where is the quiz?'))

    print(s2.speak('I have no clue!'))

    print(s4.speak('I am not sure why I am here.'))

    print(isProfessor(s1))
    print(isProfessor(s4))


if __name__ == '__main__':
    main()