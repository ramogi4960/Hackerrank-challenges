import re
"""
58
38957 TTDDHKGFA
29839 DART
47865 PERL
82072 GO
65478 ROLALP
71689 IVQWSX
22575 JAVASCRIPT
52364 DSK
88742 SBCL
72362 ARWQWZOIG
14454 PYTHON
20195 PHP
45343 KQNGX
31897 OBJECTIVEC
53444 LVDUBOTRJ
86550 OCLCLEACIU
89248 K
19908 D
36504 PASCAL
92302 SCALA
50027 OCAML
87485 CLISP
48317 CPP
21590 HASKELL
50068 GROOVY
73758 ERLANG
76801 PYTHON
37430 WHYUYM
51187 OCAML
96748 CSHARP
35981 B
51236 GZDQZF
76695 JAVA
10426 O
46486 HAQEH
41057 FD
77274 ACZVXW
25254 T
88591 JAVA
76286 DART
13421 MV
37737 ERLANG
14367 TSCFYJZKW
16793 TC
40710 FOAKFDYO
69883 CLISP
18731 PHP
55495 AAWZ
12073 PYTHON
93068 CD
71277 ERLANG
31741 JAVA
36711 FWJL
31380 LN
45548 BRAINFUCK
40387 XRJS
93770 SBCL
89030 XXGUXDZDR

INVALID
VALID
VALID
VALID
INVALID
INVALID
VALID
INVALID
VALID
INVALID
VALID
VALID
INVALID
VALID
INVALID
INVALID
INVALID
VALID
VALID
VALID
VALID
VALID
VALID
VALID
VALID
VALID
VALID
INVALID
VALID
VALID
INVALID
INVALID
VALID
INVALID
INVALID
INVALID
INVALID
INVALID
VALID
VALID
INVALID
VALID
INVALID
INVALID
INVALID
VALID
VALID
INVALID
VALID
INVALID
VALID
VALID
INVALID
INVALID
VALID
INVALID
VALID
INVALID
"""
pattern = re.compile(r"\d{5}\s(?:C|CPP|JAVA|PYTHON|PERL|PHP|RUBY|CSHARP|HASKELL|CLOJURE|BASH|SCALA|ERLANG|CLISP|LUA|BRAINFUCK|JAVASCRIPT|GO|D|OCAML|R|PASCAL|SBCL|DART|GROOVY|OBJECTIVEC)$")
validity = []
for _ in range(int(input())):
    if pattern.match(input()):
        validity.append("VALID")
    else:
        validity.append("INVALID")

print(*validity, sep="\n")