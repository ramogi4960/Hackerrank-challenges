import sys
import xml.etree.ElementTree as etree
# in this task, we are supposed t print out a score which is the total number of attributes of an xml file
# we can use the root.iter() method to find all attributes since the root.attrib method only returns the attribute
# of the parent tag


def get_attr_number(node):
    score = 0
    for i in node.iter():
        score += len(i.attrib)

    return score
    # your code goes here


if __name__ == '__main__':
    sys.stdin.readline()
    xml = sys.stdin.read()
    tree = etree.ElementTree(etree.fromstring(xml))
    root = tree.getroot()
    print(get_attr_number(root))