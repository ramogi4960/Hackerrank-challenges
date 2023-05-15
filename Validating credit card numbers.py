# in this task we are supposed to print out "VALID" for valid credit card numbers else "INVALID"
# the following conditions must be satisfied:
# -it should start with either 4, 5 or 6
# -it should have 16 characters of only digits
# -the digits may be separated by "-" in groups of 4
# -there can be no 4 or more consecutively repeated numbers
# we can start by first checking if all are digits and if there are 16 digits
# then, we can use regex to check for 4,5 or 6 at the beginning followed by 15 digits
# finally, we can check for consecutively repeated numbers using conditional statements

import re
credit_card_numbers, printing_list = [input() for _ in range(int(input()))], []
for item in credit_card_numbers:
    if re.match(r"^[456][0-9]{15}$", item):
        if any(item[i]*4 == item[i:i+4] for i in range(len(item[:-3]))):
            print("INVALID")
        else:
            print("VALID")
    elif re.search(r"^[456][0-9]{3}-{1}[0-9]{4}-{1}[0-9]{4}-{1}[0-9]{4}$", item):
        straight = "".join(item.split("-"))
        if any(straight[i]*4 == straight[i:i+4] for i in range(len(straight[:-3]))):
            print("INVALID")
        else:
            print("VALID")
    else:
        print("INVALID")
