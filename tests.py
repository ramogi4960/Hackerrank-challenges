a = set(""">>> Multi-line Comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line Comment
[if IE 9]>IE9-specific content<![endif]""")

b = set(""">>> Multi-line comment
[if IE 9]>IE9-specific content
<![endif]
>>> Data
 Welcome to HackerRank
>>> Single-line comment
[if IE 9]>IE9-specific content<![endif]""")

print(a.difference(b))