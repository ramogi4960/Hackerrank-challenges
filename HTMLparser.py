# in this ask, we take in an integer n, and n html scripts
# we are required to print out start tags, their attributes in a certain order, empty tags and end tags
# we can use the HTMLparser class from html.parser module to do this task
# if the tag has no attribute, we simply only print out the tag
# if the attribute of a tag has no value, we print the name of the attribute and "None" to represent its missing value
from html.parser import HTMLParser


class Kevin(HTMLParser):
    def handle_starttag(self, tag, attr):
        print("Start: ", tag)
        if attr is None:
            pass
        else:
            for item in attr:
                if item[1] is None:
                    print("->", item[0], "> None")
                else:
                    print("->", item[0], ">", item[1])

    def handle_startendtag(self, tag):
        print("Empty: ", tag)

    def handle_endtag(self, tag):
        print("End: ", tag)


f = []
for i in range(int(input())):
    f.append(input())

for i in f:
    file = Kevin()
    file.feed(i)
    