# in this task, we take in first name, last name, age and gender as a list in a list and print out in a certain format
# we also have to print the names sorted using the age
from operator import itemgetter

"""
Test case
3
Mike Thomson 20 M
Robert Bustle 32 M
Andria Bustle 30 F

6
Blossom Michael 9 F
Bubbles Kevin 666666666666666 F
Buttercup Jake 4444444444444444444444444444444444444444444444444444444444444444 F
Michael Blossom 8888 M
Kevin Bubbles 7777777 M
Jake Buttercup 555555555555555555555555555555 M

Ms. Blossom Michael
Mr. Michael Blossom
Mr. Kevin Bubbles
Ms. Bubbles Kevin
Mr. Jake Buttercup
Ms. Buttercup Jake

10
Blossom Blossom 10 F
Bubbles Blossom 10 F
Buttercup Blossom 9 F
Blossom Bubbles 10 F
Bubbles Bubbles 10 F
Buttercup Bubbles 200 F
Blossom Buttercup 30 F
Bubbles Buttercup 30 F
Buttercup Buttercup 10 F
Butterblossom Bubblescup 10 F

Ms. Buttercup Blossom
Ms. Blossom Blossom
Ms. Bubbles Blossom
Ms. Blossom Bubbles
Ms. Bubbles Bubbles
Ms. Buttercup Buttercup
Ms. Butterblossom Bubblescup
Ms. Blossom Buttercup
Ms. Bubbles Buttercup
Ms. Buttercup Bubbles
"""


def person_lister(f):

    def inner(people):
        a = []
        for i in people:
            i[2] = int(i[2])
        sorted_list = sorted(people, key=itemgetter(2))
        value = list(map(lambda x: f(x), sorted_list))
        return value
    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]


if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')