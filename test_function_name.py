# import etree module for parsing the xml file
import xml.etree.ElementTree as ET

# import argparse. This will let user define file and open this file as 'file'
# This defines the filename that the user inputted
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()
with open(args.filename) as file:


#This finds the HGNC name for the gene
    tree = ET.parse(file)
    root = tree.getroot()
    for lrg_locus in root.iter('lrg_locus'):
        gene = lrg_locus.text


#This specifies the default gene transcript in the transcript_name=id
#And creates a .bed file by using the gene name as the prefix
f = open("%s.bed" % (gene),"w+")
f.write("Gene name:" + gene + "\n")
for id in root.iter('id'):
    transcript_name= id.text

#This loop identifies the LRG number as coord_system,
#The exon number is identified as the label
#The coordinates for each exon are identified
#As well as the start and end coordinates for each exon
for exon in root.findall('.//fixed_annotation/transcript/exon'):
    label = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    coord_system = coordinates.get("coord_system")
    start = coordinates.get('start')
    end = coordinates.get('end')
    if coord_system == transcript_name:
        f.write(coord_system + " Exon: " + label + " Start: " + start + " End: " + end + "\n")

#The .bed file needs to be closed after creating it
f.close()

#A message is created to show the user where to find their results
print("Your results are found in the %s.bed file" % (gene))
