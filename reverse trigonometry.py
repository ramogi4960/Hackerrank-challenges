# import math
# AB = float(input())
# BC = float(input())
# angle_degrees = round(math.degrees(math.atan(AB/BC)))
# print(f"{angle_degrees}\N{DEGREE SIGN}")

import math
AB, BC = int(input()), int(input())
MC = math.sqrt((AB**2)+(BC**2))/2
print(round(math.degrees(math.asin(MC/BC))))