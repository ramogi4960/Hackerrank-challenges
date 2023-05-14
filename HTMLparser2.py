# in this task, we are supposed to print out comments adn data from lines of html code
# we shall use the HTMLParser class to create an instance

# test case
# 4
# <!--[if IE 9]>IE9-specific content
# <![endif]-->
# <div> Welcome to HackerRank</div>
# <!--[if IE 9]>IE9-specific content<![endif]-->

from html.parser import HTMLParser


class MyHtmlParser(HTMLParser):
    def handle_comment(self, data):
        print(">>> comment\n", data)
        # if "\n" in data:
        #     print(">>> Multi-line comment\n", data)
        # else:
        #     print(">>> Single-line comment\n", data)

    def handle_data(self, data):
        print(">>> Data\n", data)


html_code = """"""
for i in range(int(input())):
    html_code += input()

my_object = MyHtmlParser()  # creating an object from my sub-class created from HTMLParser class
my_object.feed(html_code)  # printing out the comments and data
