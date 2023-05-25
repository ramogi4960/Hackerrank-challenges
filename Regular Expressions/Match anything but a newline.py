# the task here is to match any string of the form abc.def.ghi.jkx where each letter is anything but a newline
# note that the length should be the same(The whole string should match the pattern)
# remember the last item of the search should not be \.
"""
Test Cases

123.123.123.1234
false

...............................
false
"""
import re
import sys

regex_pattern = r"^...\....\....\....$"
test_string = input()
match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())
