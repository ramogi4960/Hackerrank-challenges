# in this task, we are given a CSS code and we are supposed to print out all the valid Hex codes
# a valid hex code must start with #, can contain 3 or 6 digits and each digit is in the range 0 - F
# A - F letters can be lower-case
# we need to split the content that exists between { and } characters. We can do this using re
# if we use a r"[{].+[}]" it matches everything between the first { and the last }
# hence, we use r"[{][^}]"
# now we have a list of item with strings between { and } literals
# then we can use another regex to find the hex codes
"""
35
.arrow-up {
	width: 0;
	height: 0;
	border-left: 5px solid transparent;
	border-right: 5px solid transparent;

	border-bottom: 5px solid black;
}

.arrow-down {
	width: 0;
	height: 0;
	border-left: 20px solid transparent;
	border-right: 20px solid transparent;

	border-top: 20px solid #f00;
}

.arrow-right {
	width: 0;
	height: 0;
	border-top: 60px solid transparent;
	border-bottom: 60px solid transparent;

	border-left: 60px solid green;
}

#f0f {
	width: 0;
	height: 0;
	border-top: 10px solid transparent;
	border-bottom: 10px solid transparent;

	border-right:10px solid blue;
}
"""
"""
24
.custom-file-input::-webkit-file-upload-button {
  visibility: hidden;
}
.custom-file-input::before {
  content: 'Select some files';
  display: inline-block;
  background: -webkit-linear-gradient(top, #f9f9f9, #e3e3e3);
  border: 1px solid #999;
  border-radius: 3px;
  padding: 5px 8px;
  outline: none;
  white-space: nowrap;
  -webkit-user-select: none;
  cursor: pointer;
  text-shadow: 1px 1px #fff;
  font-weight: 700;
  font-size: 10pt;
}
.custom-file-input:hover::before {
  border-color: black;
}
.custom-file-input:active::before {
  background: -webkit-linear-gradient(top, #e3e3e3, #f9f9f9);
}
"""

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
    for i in re.findall(r"#[A-F0-9a-f]{6}|#[A-F0-9a-f]{3}", item):
        print(i)
    # print(*re.findall(r"#[A-F0-9a-f]{6}|#[A-F0-9a-f]{3}", item), sep="\n")
