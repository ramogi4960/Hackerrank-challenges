# in this task, we are supposed to validate if a UID is valid
# a valid UID must, have 10 characters, at least 2 uppercase letters, at least 3 digits,
# all characters must be alphanumerical, and there must be no repeating characters
# if the UID is valid, we print "VALID", else "INVALID"
# we can do this by checking if all the characters are alphanumerical, 10 in number and without repeated characters
# after passing that test, we check if there is at least 2 upper case and at least 3 digits using the length of a list
# of isupper() and isalnum() respectively
# finally, we can append a list with "VALID" or "INVALID" depending on the tests above, then print the items of that
# list

final_print_list = []
for i in range(int(input())):
    x = input()
    if len(set(x)) == 10 and x.isalnum():  # checking for repeatable, 10 characters and alphanumerical characters
        uppercase_letters, digits = [item for item in x if item.isupper()], [item for item in x if item.isdigit()]
        # checking if at least 2 uppercase and at least 3 digits
        if len(uppercase_letters) >= 2 and len(digits) >= 3:
            final_print_list.append("VALID")
    else:
        final_print_list.append("INVALID")

print(*final_print_list, sep="\n")
