# identifier is 5 digits after <a href="/questions/(identifier)/
# the Question text comes after class="question-hyperlink">(Question text)<
# the How long ago comes after class="relativetime">(How long ago)<

import re
"""
4
<h3><a href="/questions/80405/5v-regulator-power-dissipation" class="question-hyperlink">5V Regulator Power Dissipation</a></h3>
 asked <span title="2013-08-27 21:39:31Z" class="relativetime">11 hours ago</span>
 <h3><a href="/questions/80407/about-power-supply-of-opertional-amplifier" class="question-hyperlink">about power supply of opertional amplifier</a></h3>
 asked <span title="2013-08-27 21:49:14Z" class="relativetime">11 hours ago</span>
"""

markup = [input() for _ in range(int(input()))]
identifier = re.compile(r"(?<=href=\"\/questions\/)\d{5}(?=\/)")
question_text = re.compile(r"(?<=hyperlink\">).+?(?=<)")
how_long_ago = re.compile(r"(?<=class=\"relativetime\">).+?(?=<)")
a, b, c = [], [], []
for item in markup:
    if identifier.search(item) and question_text.search(item):
        for t in list(identifier.findall(item)):
            a.append(t)
        for t in list(question_text.findall(item)):
            b.append(t)
    elif how_long_ago.search(item):
        for t in list(how_long_ago.findall(item)):
            c.append(t)

for number in range(len(a)):
    print(a[number], b[number], c[number], sep=";")
