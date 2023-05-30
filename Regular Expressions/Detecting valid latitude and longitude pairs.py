import re
"""
Test Case
12
(75, 180)
(+90.0, -147.45)
(77.11112223331, 149.99999999)
(+90, +180)
(90, 180)
(-90.00000, -180.0000)
(75, 280)
(+190.0, -147.45)
(77.11112223331, 249.99999999)
(+90, +180.2)
(90., 180.)
(-090.00000, -180.0000)

30
(-24, -93)
(-24.157721, -93.157721)
(-79, -55)
(-79.540667, -55.540667)
(-116, -99)
(-116.639280, -99.639280)
(-122, -196)
(-122.85186, -196.85186)
(-67, -70)
(-67.233682, -70.233682)
(-64, -67)
(-64.780557, -67.780557)
(-65, -271)
(-65.347042, -271.347042)
(-32, -85)
(-32.84880, -85.84880)
(-110, -6)
(-110.158590, -6.158590)
(-130, -219)
(-130.581178, -219.581178)
(-88, -241)
(-88.344600, -241.344600)
(-6, -165)
(-6.871826, -165.871826)
(-98, -40)
(-98.122626, -40.122626)
(-6, -172)
(-6.377934, -172.377934)
(-147, -266)
(-147.357525, -266.357525)
"""
pattern = r"\([-\+]?\d{1,2}(?:\.\d+)?,\s[-\+]?\d{1,3}(?:\.\d+)?\)"
l = []
for _ in range(int(input())):
    f = input()
    if re.search(pattern, f):
        for item in list(re.findall(pattern, f)):
            n = item.split(",")
            if -90 <= float(n[0][1:]) <= 90 and -180 <= float(n[1][:-1]) <= 180:
                l.append("Valid")
            else:
                l.append("Invalid")
    else:
        l.append("Invalid")


print(*l, sep="\n")
