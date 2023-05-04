# let z be a complex number representing a polar coordinate
# the angle between the line and the x-axis is given by phase(z)
# the length of the line from origin to the polar coordinate is given by abs(z)
from cmath import phase
z = complex(1+2j)
print(phase(z))
print(abs(z))