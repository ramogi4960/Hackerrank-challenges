class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def calculate(self):
        a = sum(self.scores) / len(scores)
        if a < 40:
            return "T"
        elif 40 <= a < 55:
            return "D"
        elif 55 <= a < 70:
            return "P"
        elif 70 <= a < 80:
            return "A"
        elif 80 <= a < 90:
            return "E"
        elif 90 <= a <= 100:
            return "O"


line = input().split()
firstName, lastName, idNum = line[0], line[1], line[2]
numScores = int(input())  # not needed for Python
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())