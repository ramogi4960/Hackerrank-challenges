# in this task, we are given  a number of students N, and a number of subjects X that each
# student must do.
# we are supposed to print out the average marks of each student, vertically
# First we need to put the marks each student got in a particular subject in a list.
# so then there will be X lists of N items. In each list, the index of the items represent the
# student ID. So using the zip() function, we can get the average of each student
N, M = list(map(int, input().split()))
list_zip = []
for i in range(M): # iterate through students as we enter their marks for each subject
    a = list(map(float, input().split()))
    list_zip.append(a)

# now we use zip() to find the average of each student/index
for item in list(zip(*list_zip)):
    print(sum(item)/M)
