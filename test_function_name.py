import xml.etree.ElementTree as ET
tree = ET.parse('LRG_1.xml')
root = tree.getroot()

#Searches the whole xml file for the root called lrg_locus and prints the text in that line, which is the HGNC gene name
for lrg_locus in root.iter('lrg_locus'):
      print (lrg_locus.text)
