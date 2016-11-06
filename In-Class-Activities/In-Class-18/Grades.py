from Student import *


class Grades(object):
    """A mapping from students to a list of grades"""

    def __init__(self):
        """Create empty grade book"""
        self.students = []  # list of Student objects
        self.grades = {}    # maps idNum -> list of grades
        self.isSorted = True  # true if self.students is sorted

    def addStudent(self, student):
        """Assumes: student is of type Student
           Add student to the grade book"""
        if student in self.students:
            raise ValueError('Duplicate student')
        self.students.append(student)
        self.grades[student.idNum] = []
        self.isSorted = False

    def addGrade(self, student, grade):
        """Assumes: grade is a float
           Add grade to the list of grades for student"""
        try:
            self.grades[student.idNum].append(grade)
        except KeyError:
            raise ValueError('Student not in grade book')

    def getGrades(self, student):
        """Return a list of grades for student"""
        try:    # return copy of student's grades
            return self.grades[student.idNum][:]
        except KeyError:
            raise ValueError('Student not in grade book')

    def allStudents(self):
        """Return a list of the students in the grade book"""
        if not self.isSorted:
            self.students.sort()
            self.isSorted = True

        # return copy of list of students
        return self.students[:]


def gradeReport(course):
    """Assumes: course if of type grades"""
    report = []
    for s in course.allStudents():
        tot = 0.0
        numGrades = 0
        for g in course.getGrades(s):
            tot += g
            numGrades += 1
        try:
            average = tot / numGrades
            report.append(str(s) + '\'s mean grade is ' + str(average))
        except ZeroDivisionError:
            report.append(str(s) + ' has no grades')
    return '\n'.join(report)


def main():
    ug1 = UG('Jason Wang', 2018)
    ug2 = UG('Hunter Schilb', 2017)
    ug3 = UG('Wendy Posada', 2017)
    ug4 = UG('Mark Oh', 2017)
    g1 = Grad('Matt Damon')
    g2 = Grad('Ben Affleck')

    mis3640 = Grades()
    mis3640.addStudent(g1)
    mis3640.addStudent(ug2)
    mis3640.addStudent(ug1)
    mis3640.addStudent(g2)
    mis3640.addStudent(ug4)
    mis3640.addStudent(ug3)

    mis3640.addGrade(g1, 100)
    mis3640.addGrade(g2, 25)
    mis3640.addGrade(ug1, 95)
    mis3640.addGrade(ug2, 85)
    mis3640.addGrade(ug3, 75)

    print(gradeReport(mis3640))

    mis3640.addGrade(g1, 90)
    mis3640.addGrade(g2, 45)
    mis3640.addGrade(ug1, 80)
    mis3640.addGrade(ug2, 75)

    print(gradeReport(mis3640))

if __name__ == '__main__':
    main()