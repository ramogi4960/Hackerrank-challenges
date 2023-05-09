# in this task, we first use a regex pattern to validate if an email is valid.
# after that, we pass the email into email.utils.formataddr to print it out accordingly
import re
from email.utils import parseaddr, formataddr
p = re.compile("^[A-Za-z]{1}[A-Za-z0-9-_\.]+@{1}[A-Za-z]+\.{1}[A-Za-z]{1,3}$")
items_lists = [input().split() for _ in range(int(input()))]
# email_list = [item[1].rstrip(">").lstrip("<") for item in items_lists]
# true_emails = [i for i in email_list if p.search(i) is not None]
for i in items_lists:
    if p.search(i[1].rstrip(">").lstrip("<")) is not None:
        print(formataddr((i[0], i[1].rstrip(">").lstrip("<"))))
