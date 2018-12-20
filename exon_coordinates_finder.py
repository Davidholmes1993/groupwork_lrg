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
f.write("Gene name:" + gene + "\n" + "Chrom" + "\t" "ChromStart" + "\t" + "ChromEnd" + "\t" "Exon" + "\t" + "Strand" + "\n")
for id in root.iter('id'):
    transcript_name= id.text


# This will create the genomic coordinates for each exon start and end, only for
# the genome build 37, and only for a forward strand
# need to do the addition of the integers before the print line
for mapping in root.findall('.//updatable_annotation/annotation_set/mapping'):
    genome_build = mapping.get("coord_system")
    mapping_span = mapping.find('mapping_span').attrib
    if genome_build == "GRCh37.p13":
        strand = mapping_span.get('strand')
        chromosome_number = mapping.get("other_name")
        int_chromosome_number=int(chromosome_number)
        chromosome_start = mapping.get("other_start")
        int_chromosome_start=int(chromosome_start)
        chromosome_end = mapping.get("other_end")
        int_chromosome_end=int(chromosome_end)


# This loop identifies the LRG number as coord_system,
# The exon number is identified as the label
# The coordinates for each exon are identified
# As well as the start and end coordinates for each exon
for exon in root.findall('.//fixed_annotation/transcript/exon'):
    label = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    coord_system = coordinates.get("coord_system")
    #strand = coordinates.get('strand')
    start = coordinates.get('start')
    int_start = int(start)
    end = coordinates.get('end')
    int_end = int(end)
    if strand == '1':
        final_chromosome_start = str(int_chromosome_start -1 + int_start)
        final_chromosome_end = str(int_chromosome_start -1 + int_end)
    elif strand =='-1':
        final_chromosome_start = str(int_chromosome_end +1 - int_start)
        final_chromosome_end = str(int_chromosome_end +1 - int_end)
    if coord_system == transcript_name:
        f.write(chromosome_number + "\t" + final_chromosome_start + "\t" + final_chromosome_end + "\t" + label + "\t" + strand + "\n")

# The .bed file needs to be closed after creating it
f.close()

# A message is created to show the user where to find their results
print("Your results are found in the %s.bed file" % (gene))
