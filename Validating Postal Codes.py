# the postal code should be within range(100000, 1000000)
# the postal code can only have one alternating repetitive number
import re

regex_integer_in_range = r"[0-9]{6}"	# Do not delete 'r'.
regex_alternating_repetitive_digit_pair = r"(\d){1}"	# Do not delete 'r'.



P = input()

print (bool(re.match(regex_integer_in_range, P)) and len(re.findall(regex_alternating_repetitive_digit_pair, P)) < 2)