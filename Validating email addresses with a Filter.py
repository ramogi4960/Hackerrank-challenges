# this is a way of validating email addresses.
# first we take in an email as an input. We need to split the email using a re.split() function
# after splitting, we can place the username, extension and website name as separate variables
# we can then check if each item is correctly entered
import re


def fun(s):
    reg_pattern = r"[@.]"
    split_email = list(re.split(reg_pattern, s))
    if len(split_email) == 3:
        if split_email[2].isalpha() and len(split_email[2]) < 4:
            if split_email[1].isalnum():
                pattern = r"[_-]"
                t = re.split(pattern, split_email[0])
                for item in t:
                    if item.isalnum():
                        return True
        else:
            False


def filter_mail(emails):
    return list(filter(fun, emails))


if __name__ == '__main__':
    n = int(input())
    emails = []
    for _ in range(n):
        emails.append(input())

filtered_emails = filter_mail(emails)
filtered_emails.sort()
print(*filtered_emails, sep="\n")
