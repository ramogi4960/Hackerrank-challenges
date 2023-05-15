# in this task, we are given html code and have to print out comments and data in a particular way
# multi-line and single-line comments should be printed in a different manner
# we need to find out if the comment is a multi-line or not
# we can join lines of the html code with \n for items that fulfill defined conditions for a multi-line
# if not, we join the lines with ""

from html.parser import HTMLParser


class Remy(HTMLParser):
    def handle_comment(self, data):
        if "\n" in data:
            print(f">>> Multi-line comment\n{data}")
        else:
            print(f">>> Single-line comment\n{data}")

    def handle_data(self, data):
        print(f">>> Data\n{data}")


html_code = [input() for _ in range(int(input()))]
new_html_code = []
for i in range(len(html_code)): # section to handle multi-line comments in a different way
    if html_code[i][:4] == "<!--" and html_code[i][-3:] != "-->":
        feeder = [html_code[i]]
        for item in html_code[i+1:]:
            feeder.append(item)
            if item[-3:] == "-->":
                break
        new_html_code.append("\n".join(feeder))
    elif html_code[i][:4] == "<!--" and html_code[i][-3:] == "-->":
        new_html_code.append(html_code[i])
    elif html_code[i][:4] != "<!--" and html_code[i][-3:] == "-->":
        pass
    else:
        new_html_code.append(html_code[i])

my_object = Remy()
my_object.feed("".join(new_html_code))