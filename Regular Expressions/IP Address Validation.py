# in this task, we are supposed to check if a string is an IPv6 or IPv4 address
# IPv4 addresses are in the form A.B.C.D where A,B,C and D are integers in range(0, 256)
# IPv6 addresses are 8 groups of 16bit hexagonal numbers separated by :
import re
ipv6 = r"^[0-9a-f]{1,4}(:[0-9a-f]{1,4}){7}$"
ip_list = [input() for _ in range(int(input()))]
for item in ip_list:
    if re.match(ipv6, item):
        print("IPv6")
    elif len(item.split(".")) == 4:
        a = True
        for i in item.split("."):
            if int(i) in range(0, 256):
                pass
            else:
                a = False
                break
        print("IPv4" if a else "Neither")
    else:
        print("Neither")
