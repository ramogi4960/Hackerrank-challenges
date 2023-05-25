# you have a test string S. Your task is to match XXxXXxXX where x denotes whitespace and X non-whitespace
Regex_Pattern = r"(\S\S\s){2}\S\S"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())