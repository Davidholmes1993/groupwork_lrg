# import etree module for parsing the xml file
import xml.etree.ElementTree as ET

# import argparse. This will let user define file and open this file as 'file'
import argparse

# This defines the filename that the user inputted
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# A test to check if the file is in the correct directory
#If not it will tell the user and terminate the program
try:
    f = open(args.filename)
except FileNotFoundError:
  print("ERROR: This file does not exist in this directory" + "\n"  + "Please make sure your file is saved in groupwork_lrg directory")
  exit()

# Puts args into string format so that file extension can be tested
name_of_file = str(args)

# If statement that tests whether or not the the file type is .xml. If the file is not correct it will let the user know and terminate the programme
if name_of_file.endswith(".xml')"):
    pass
else:
    print("ERROR: Invalid file type. File must have extension .xml")
    exit()

# This uses argparse to open the file that the user has inputted
with open(args.filename) as file:

# This finds the HGNC name for the gene
    tree = ET.parse(file)
    root = tree.getroot()
    for lrg_locus in root.iter('lrg_locus'):
        gene = lrg_locus.text


# This specifies the default gene transcript in the transcript_name=id
# And creates a .bed file by using the gene name as the prefix
f = open("%s.bed" % (gene),"w+")
f.write("Gene name:" + gene + "\n")
for id in root.iter('id'):
    transcript_name= id.text

# This loop identifies the LRG number as coord_system,
# The exon number is identified as the label
# The coordinates for each exon are identified
# As well as the start and end coordinates for each exon
for exon in root.findall('.//fixed_annotation/transcript/exon'):
    label = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    coord_system = coordinates.get("coord_system")
    start = coordinates.get('start')
    end = coordinates.get('end')
    if coord_system == transcript_name:
        f.write(coord_system + " Exon: " + label + " Start: " + start + " End: " + end + "\n")

# The .bed file needs to be closed after creating it
f.close()

# A message is created to show the user where to find their results
print("Your results are found in the %s.bed file" % (gene))
