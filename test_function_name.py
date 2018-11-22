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
        gene = lrg_locus.text

f = open("%s.bed" % (gene),"w+")

for id in root.iter('id'):
    transcript_name= id.text

#for exon in root.findall('.//fixed_annotation/transcript/exon'):
 #   label = exon.get('label')
  #  f.write("Exon: " + label + "\n")

for exon in root.findall('.//fixed_annotation/transcript/exon'):
    label = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    coord_system = coordinates.get("coord_system")
    start = coordinates.get('start')
    end = coordinates.get('end')
    if coord_system == transcript_name:
        f.write(coord_system + " Exon: " + label + " Start: " + start + " End: " + end + "\n")


f.close() 
