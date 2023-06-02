import re
"""
<li style="-moz-float-edge: content-box">... that <a href="/wiki/Orval_Overall" title="Orval Overall">Orval Overall</a> <i>(pictured)</i> is the only <b><a href="/wiki/List_of_Major_League_Baseball_pitchers_who_have_struck_out_four_batters_in_one_inning" title="List of Major League Baseball pitchers who have struck out four batters in one inning">Major League Baseball player to strike out four batters in one inning</a></b> in the <a href="/wiki/World_Series" title="World Series">World Series</a>?</li>
"""
x = input()
pat = re.compile(r"(?<=<)(\w+)(\s.*?)(?=>)")
l = list(pat.findall(x))
for i in l:
    att, tag = [], i[0]
    for item in list(re.findall(r"(?<=\s)\w*?(?==)", i[1])):
        att.append(item)
    a = ",".join(att)
    print(f"{tag}:{a}")