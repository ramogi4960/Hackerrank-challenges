# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
N = int(input("Enter Odd Number: "))
M = N*3
s = ".|."
shape = "-"
name = input("Enter Name: ")
for i in range(N):
    if i == math.floor(N/2):
        print(name.center(M, shape))
        break
    print(s.center(M, shape))
    s += ".|..|."

f = s.replace(".|.", "", 2)
for i in range(N):
    if i > math.floor(N/2):
        print(f.center(M, shape))
        if i == N-1:
            break
        f = f.replace(".|.", "", 2)
