import xml.etree.ElementTree as ET
tree = ET.parse('LRG_1.xml')
root = tree.getroot()


name=root[0][4][0].text
list=name.split()
print (list[-1])


