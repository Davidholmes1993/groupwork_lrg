# import etree module for parsing the xml file
import xml.etree.ElementTree as ET

# import argparse. This defines the XML file that the user inputted
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('filename')
args = parser.parse_args()

# import datetime to enable the LRG parser program to give the date and time in the output filename
import datetime
output_time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")

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

# This defines the HGNC name of the gene to be used in the output filename
    tree = ET.parse(file)
    root = tree.getroot()
    for lrg_locus in root.iter('lrg_locus'):
        gene = lrg_locus.text

# This specifies the LRG number to be used in the output filename
# And creates a .bed file with the filename of the lrg number, the gene and the date and time the file was created
# A header row is created for the bed file to label each column
for id in root.iter('id'):
    lrg_number= id.text
f = open("%s%s%s%s%s.bed" % (lrg_number,"_", gene, "_", output_time),"w+")
f.write("Chrom" + "\t" "ChromStart" + "\t" + "ChromEnd" + "\t" "Exon" + "\t" + "Strand" + "\n")


# This will find the genomic coordinates for the whole gene to be used later on to
# add or subtract the LRG coordinates in order to give the genomic coordinates of each exon.
# The chromosome number is identified, and the strand is identified as forward or reverse strand.
# The coordinates are found only for the genome build GRCh37.p13
for mapping in root.findall('.//updatable_annotation/annotation_set/mapping'):
    genome_build = mapping.get("coord_system")
    mapping_span = mapping.find('mapping_span').attrib
    if genome_build == "GRCh37.p13":
        strand = mapping_span.get('strand')
        chromosome_number = mapping.get("other_name")
        genomic_start = int(mapping.get("other_start"))
        genomic_end = int(mapping.get("other_end"))

# This loop identifies the transcript name and only uses the default transcript that matches the LRG name,
# The exon number is identified
# As well as the start and end genomic coordinates for each exon, depending on if it is a forward or reverse strand
# by adding or subtracting the LRG exon coordinates to/from the genomic coordinates of the whole gene
for exon in root.findall('.//fixed_annotation/transcript/exon'):
    exon_number = exon.get('label')
    coordinates = exon.find('coordinates').attrib
    transcript_name = coordinates.get("coord_system")
    exon_start = int(coordinates.get('start'))
    exon_end = int(coordinates.get('end'))
    if strand == '1':
        final_genomic_start = str(genomic_start + exon_start -1)
        final_genomic_end = str(genomic_start + exon_end -1)
        strand_definition = "+"
    elif strand =='-1':
        final_genomic_start = str(genomic_end - exon_start +1)
        final_genomic_end = str(genomic_end - exon_end +1)
        strand_definition = "-"
    if transcript_name == lrg_number:
        f.write(chromosome_number + "\t" + final_genomic_start + "\t" + final_genomic_end + "\t" + exon_number + "\t" + strand_definition + "\n")

# The .bed file needs to be closed after creating it
f.close()

# A message is created to show the user where to find their results in the output file after the LRG parser program is finished.
print("Your results are found in the %s%s%s%s%s.bed file" % (lrg_number,"_", gene, "_", output_time))
