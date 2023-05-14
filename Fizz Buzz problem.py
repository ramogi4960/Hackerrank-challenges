# the fizz buzz problem is a common interview question
# We print "Fizz" if a number is divisible by 3, "Buzz" if the number is divisible by 5, and "FizzBuzz" if the number is
# divisible by both 3 and 5. If it's not divisible by any of them, we print out "Not divisible"
number = int(input("Enter number to be checked: "))
if number%3 == 0:
    print("Fizz")
elif number%5 == 0:
    print("Buzz")
elif number%3 == 0 and number%5 == 0:
    print("Fizz Buzz")
else:
    print("Not divisible by 3 or 5 or both")
