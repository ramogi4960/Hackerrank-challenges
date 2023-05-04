# in this problem, we are trying to use exceptions. Dividing an int by 0 generates a ZeroDivisionError
# dividing a number by a non-int generates a SyntaxError
# exceptions allow us to try executing a line of code, then execute another line of code
# if the first one generates an error

t = int(input())
list1 = [input().split() for i in range(t)]

for i in range(t):
    try:
        print(int(list1[i][0])//int(list1[i][1]))
    except ZeroDivisionError as e:
        print("Error Code:", e)
    except SyntaxError as s:
        print("Error Code:", s)
    except ValueError as v:
        print("Error Code:", v)

