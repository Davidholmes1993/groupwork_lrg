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
# At the top of the bed file the gene name, and a header row is printed
f = open("%s.bed" % (gene),"w+")
f.write("Gene name:" + gene + "\n" + "Chrom" + "\t" "ChromStart" + "\t" + "ChromEnd" + "\t" "Exon" + "\t" + "Strand" + "\n")
for id in root.iter('id'):
    transcript_name= id.text

# This will find the genomic coordinates for the gene and converts them into integers to be used later on to
# add or subtract the LRG coordinates integers in order to give the genomic corrdinates of the exon.
# The chromosome number is identified, and the strand is identified as forward or reverse
# only for the genome build 37
for mapping in root.findall('.//updatable_annotation/annotation_set/mapping'):
    genome_build = mapping.get("coord_system")
    mapping_span = mapping.find('mapping_span').attrib
    if genome_build == "GRCh37.p13":
        strand = mapping_span.get('strand')
        chromosome_number = mapping.get("other_name")
        int_chromosome_number=int(chromosome_number)
        genomic_start = mapping.get("other_start")
        int_genomic_start=int(genomic_start)
        genomic_end = mapping.get("other_end")
        int_genomic_end=int(genomic_end)

# This loop identifies the LRG number as coord_system,
# The exon number is identified as the label
# As well as the start and end genomic coordinates for each exon, depending on if it is a forward or reverse strand
# by adding or subtracting them alongside the genomic coordinates of the gene
for exon in root.findall('.//fixed_annotation/transcript/exon'):
    label = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    coord_system = coordinates.get("coord_system")
    start = coordinates.get('start')
    int_start = int(start)
    end = coordinates.get('end')
    int_end = int(end)
    if strand == '1':
        final_genomic_start = str(int_genomic_start -1 + int_start)
        final_genomic_end = str(int_genomic_start -1 + int_end)
    elif strand =='-1':
        final_genomic_start = str(int_genomic_end +1 - int_start)
        final_genomic_end = str(int_genomic_end +1 - int_end)
    if coord_system == transcript_name:
        f.write(chromosome_number + "\t" + final_genomic_start + "\t" + final_genomic_end + "\t" + label + "\t" + strand + "\n")

# The .bed file needs to be closed after creating it
f.close()

# A message is created to show the user where to find their results
print("Your results are found in the %s.bed file" % (gene))
