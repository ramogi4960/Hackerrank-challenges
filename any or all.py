# our task is to check if all int in a list are positive, and if any of them is a palindrom number
# to check if each number is a positive int, we check if int>0
# to check if it's a palindrome number we check if str(int) == sorted(str(int), reverse=True)
# to do this, we can first check for positive numbers in the list, and append another list
# of boolean values if all the ints are positive, else we append false
# secondly, we check if any of the integers is a palindrome and append the list with it's respective boolean
# finally, we use all() on the boolean list
N, L = int(input()), list(map(int, input().split()))
print(all(i >= 0 for i in L) and any((str(i) == str(i)[::-1]) for i in L))