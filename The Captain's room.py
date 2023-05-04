# we are given the size of each group, and a list of room numbers allocated to each
# group and the captain
# in the list of room numbers, each number is goung to be repeated (number of groups)times,
# except the captain's room.
# so the number of groups = (len(list of room numbers)-1)/size of each group
# we can find the captains room using Counter in collections module
# we check each item in a dict of counter by using a list of keys from that Counter
from collections import Counter
K, rooms = int(input()), list(map(int, input().split()))
count_dict = dict(Counter(rooms))
count_keys = list(count_dict.keys())
for captain in count_keys:
    if count_dict[captain] == 1:
        print(captain)
