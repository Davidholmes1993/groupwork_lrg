# import etree module
import xml.etree.ElementTree as ET

# import argparse. This will let user define file and open this file as 'file'

import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as file:
    """
    Searches the whole xml file for the root called lrg_locus and prints the text in that 
    line, which is the HGNC gene name
    """
    tree = ET.parse(file)
    root = tree.getroot()
    for lrg_locus in root.iter('lrg_locus'):
        print (lrg_locus.text)


