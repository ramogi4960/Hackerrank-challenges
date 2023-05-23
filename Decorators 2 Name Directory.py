# in this task, we take in first name, last name, age and gender as a list in a list and print out in a certain format
# we also have to print the names sorted using the age
from operator import itemgetter

"""
Test case
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F
"""


def person_lister(f):
    def inner(people):
        sorted_list = sorted(people, key=itemgetter(2))

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')
