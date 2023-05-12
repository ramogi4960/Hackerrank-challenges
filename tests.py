import re
x = re.compile(r"M{,3}(D?C{,3}|C[DM])?(L?X{,3}|X[LC])?(V?I{,3}|I[VX])?$")
print(bool(x.match(input("Enter string to check if it's a valid roman number: "))))
