# in this task we have a test string S
# we are supposed to match xxXxxXxxxx where x is a digit, and X is anything but a digit
import re
Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"
print(str(bool(re.search(Regex_Pattern, input()))).lower())