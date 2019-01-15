'''
import pytest module
import xml.etree.ElementTree module
'''
import pytest
import xml.etree.ElementTree as ET

'''
This imports functions from the programme exon_coordinates_finder
'''
from exon_coordinates_finder import (find_gene, get_lrg_number, find_genomic_coord)

'''
This function will test that when given the file LRG_1.xml the find_gene function gives
COL1A1 as an answer
'''
def test_find_gene():
	tree=ET.parse('LRG_1.xml')
	root = tree.getroot()
	assert find_gene(root) == 'COL1A1'

'''
This function will test that when given the file LRG_1.xml the get_lrg_number function gives
LRG_1 as an answer
'''
def test_get_lrg_number():
	tree=ET.parse('LRG_1.xml')
	root = tree.getroot()
	assert get_lrg_number(root) == 'LRG_1'

'''
This function will test that when given the file LRG_1.xml and chosen genomic build 37 the 
find_genomic_coord function gives strand = -1, chromosome_number = 17, genomic_start = 48259457
and genomic_end = 48284000
'''
def test_GRCh37_find_genomic_coord():
	tree=ET.parse('LRG_1.xml')
	root = tree.getroot()
	build = '37'
	assert find_genomic_coord(root, build) == ('-1', '17', 48259457, 48284000)

'''
This function will test that when given the file LRG_1.xml and chosen genomic build 38 the 
find_genomic_coord function gives strand = -1, chromosome_number = 17, genomic_start = 50182096
and genomic_end = 50206639
'''
def test_GRCh38_find_genomic_coord():
	tree=ET.parse('LRG_1.xml')
	root = tree.getroot()
	build = '38'
	assert find_genomic_coord(root, build) == ('-1', '17', 50182096, 50206639)
