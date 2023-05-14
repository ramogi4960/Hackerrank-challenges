# in this task, we are given a CSS code and we are supposed to print out all the valid Hex codes
# a valid hex code must start with #, can contain 3 or 6 digits and each digit is in the range 0 - F
# A - F letters can be lower-case
# we need to split the content that exists between { and } characters. We can do this using re
# if we use a r"[{].+[}]" it matches everything between the first { and the last }
# hence, we use r"[{][^}]"
# now we have a list of item with strings between { and } literals
# then we can use another regex to find the hex codes

"""
11
#BED
{
color: #FfFdF8; background-color: #aef;
font-size: 123px;
background: -webkit-linear-gradient(top, #f9f9ff9, bottom, #fff)
}
#Cab
{
background-color: #ABC;
border: 2px dashed #fff;
}
"""

import re
css_code = ""
for i in range(int(input())):
    css_code += input()

pat = re.compile(r"[{][^}]+")
for item in pat.findall(css_code):
    print(*re.findall(r"#[A-F0-9a-f]{6}|#[A-F0-9a-f]{3}", item), sep="\n")
