# the positive look ahead matches if the match is followed by a certain pattern (?=pattern)
Regex_Pattern = r'o(?=oo)'

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))

# the negative lookahead matches if the match is not followed by a certain match(?!pattern)
Regex_Pattern = r"(.)(?!\1)"

import re

Test_String = input()

match = re.findall(Regex_Pattern, Test_String)

print("Number of matches :", len(match))