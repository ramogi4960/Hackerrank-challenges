# in this task, we are supposed to print html tags and their attributes if any
from html.parser import HTMLParser


class Kevin(HTMLParser):
    def handle_starttag(self, tag, attr):
        print(tag)
        if attr:
            for item in attr:
                print("->", item[0], ">", item[1])


html_code = [input() for _ in range(int(input()))]

my_object = Kevin()
my_object.feed("".join(html_code))
