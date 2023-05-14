from html.parser import HTMLParser


class Kevin(HTMLParser):
    def handle_starttag(self, tag, attr):
        print("The start tag is:", tag)
        for item in attr:
            print("->", item[0], ">", item[1])

    def handle_endtag(self, tag):
        print(("The end tag is: ", tag))

    def handle_startendtag(self, tag, attr):
        print("")


file = Kevin()
file.feed("<html lang='en' dir='ltr'><head><meta charset='utf-8'><title></title></head><body></body></html>")

# file.feed("<html>"
#           "<head>"
#           "<title>"
#           "</title>"
#           "</head>"
#           "<body colo>"
#           "</body>"
#           "</html>")
