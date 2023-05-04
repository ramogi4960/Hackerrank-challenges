# we are supposed to get the average marks of the students
# we can do this by adding the values under 'marks' and dividing it by the input int
# these marks together with other collumn data will be stored in a namedtuple
from collections import namedtuple
students_num = int(input())
Student = namedtuple('Student', input().split())
marks = sum([int(Student(*input().split()).MARKS) for _ in range(students_num)])
print('%.2f' % (marks / students_num))

