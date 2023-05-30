# import re
# import sys
#
# if __name__ == '__main__':
#     codes = sys.stdin.read()
#     for i in re.findall(r'\/\/.*|\/\*.*(?:[^\*\/]\n.*)*(?<=\*\/)',codes):
#         print('\n'.join([j.strip() for j in re.split(r'\n',i)]))