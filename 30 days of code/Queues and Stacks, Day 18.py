import sys
# in this task, we are supposed to check if a certain input() is a palindrome.
# a palindrome is a word that remains the same when printed in reverse, like level, or racecar
# so I first created instance variables for the object instance, then functions for filling the queue and stack.
# afterwords, I created functions for dequeue and removing the first item of the stack as the value is returned
# if the returned values are all the same, then the word is a palindrome


class Solution:
    def __init__(self):
        self.stack = []
        self.queue = []

    def pushCharacter(self, char):
        self.stack.append(char)

    def enqueueCharacter(self, char):
        self.queue.append(char)

    def popCharacter(self):
        a = self.stack[0]
        del self.stack[0]
        return a

    def dequeueCharacter(self):
        a = self.queue[-1]
        self.queue.pop()
        return a


# read the string s
s = input()
# Create the Solution class object
obj = Solution()

l = len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
for i in range(l // 2):
    if obj.popCharacter() != obj.dequeueCharacter():
        isPalindrome = False
        break

# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
