# identifier is 5 digits after <a href="/questions/(identifier)/
# the Question text is right after the identifier and ends with "
# the How long ago comes after class="relativetime">(How long ago)<

"""
4
<h3><a href="/questions/80405/5v-regulator-power-dissipation" class="question-hyperlink">5V Regulator Power Dissipation</a></h3>
 asked <span title="2013-08-27 21:39:31Z" class="relativetime">11 hours ago</span>
 <h3><a href="/questions/80407/about-power-supply-of-opertional-amplifier" class="question-hyperlink">about power supply of opertional amplifier</a></h3>
 asked <span title="2013-08-27 21:49:14Z" class="relativetime">11 hours ago</span>
"""
import re
markup, l, m = [input() for _ in range(int(input()))], [], []
pattern = re.compile(r"(?<=href=\"\/questions\/)\d{5}\/.+?(?=\")")
how_long_ago = re.compile(r"(?<=class=\"relativetime\">).+?(?=<)")
for item in markup:
    if pattern.search(item):
        for i in list(pattern.findall(item)):
            l.append(i)

    if how_long_ago.search(item):
        for i in list(how_long_ago.findall(item)):
            m.append(i)

for n in range(len(l)):
    f = l[n].split("/")
    print(f[0], f[1], m[n], sep=";")
