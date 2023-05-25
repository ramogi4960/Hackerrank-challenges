Regex_Pattern = r'(ok)\1\1'
# finding 3 or more repetitions of "ok"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())