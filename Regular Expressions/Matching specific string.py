# you have a string S. Your task is to match "hackerrank"
import re
Regex_Pattern = r'hackerrank'
Test_String = input()
match = re.findall(Regex_Pattern, Test_String)
print("Number of matches :", len(match))
