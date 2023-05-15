# # using re to find consecutives
# # ??????
# # let me think
#
# from html.parser import HTMLParser
# import re
#
# html_code, new_html_code = [input() for _ in range(int(input()))], []
# for number in range(len(html_code)):
#     if re.search(r"^<!--.*", html_code[number]):
#         new_html_code.append(html_code[number] + "\n")
#     elif re.search(r".*-->$", html_code[number]):
#         new_html_code.append(html_code[number])
#     elif re.search(r"\\n$", html_code[number - 1]) and number > 0:
#         new_html_code.append(html_code[number] + "\n")
#     else:
#         new_html_code.append(html_code[number])
#
#
# class My_Parser(HTMLParser):
#     def handle_comment(self, data):
#         if "\n" in data:
#             print(f">>> Multi-line Comment\n{data}")
#         else:
#             print(f">>> Single-line Comment\n{data}")
#
#     def handle_data(self, data):
#         print(f">>> Data\n{data}")
#
#
# my_object = My_Parser()
# my_object.feed("".join(new_html_code))
