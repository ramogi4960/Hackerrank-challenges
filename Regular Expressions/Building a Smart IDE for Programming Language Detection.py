# in this task, we are supposed to determin whether a piece o input is written in either C, Java or Python
import re
import sys
java = re.compile(r"import\sjava|System\.out\.println|System\.exit")
C = re.compile(r"#include|scanf|return 0;")
test = sys.stdin.read()

if java.search(test):
    print("Java")
elif C.search(test):
    print("C")
else:
    print("Python")