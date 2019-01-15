<h1>LRG parser</h1>
<h6>An LRG parser python program created by David Holmes and Maria Lock for the BIOL68400 Programming group work with the University of Manchester</h6>
<h2>Purpose</h2>
A python program to parse an XML file and output into a bed file the chromosome number, the start and end genomic coordinates for each exon, the exon number and if it is a forward or reverse strand. The user can select the coordinates using either genome build GRCh37 or GRCh38 when prompted.

<h2>Usage</h2>
Suitable for use with python 3. Requires the LRG xml file to be saved in the same local folder. See instructions below for detailed information

Example: `python exon_coordinates_finder.py <your LRG_*.xml file here>`
<h2>Instructions</h2>

To download and use our repository and run our exon coordinates finder program,
type: `git init` into your command line, and then type:
`git clone https://github.com/Davidholmes1993/groupwork_lrg.git`

For the gene you want to investigate on https://www.lrg-sequence.org/ ,
download the .xml file for that gene and save this into the same folder from
the repository from Github, the groupwork_lrg folder.

When in the repository, on your command line, type python exon_coordinates_finder.py
as well as the name of the LRG file that you have downloaded and saved
with a space in between the program and filename.
For example, to analyse LRG_1 type into the command line:

`python exon_coordinates_finder.py LRG_1.xml`

You will receive a message for the name of the file where your results
are stored in a .bed file, which will be found in the repository folder.
Open this file to see the information about the gene in the LRG file in a
tab delimited format showing the chromosome, genomic coordinates for the
start and end coordinates of each exon, the exon number, and if the strand is
forward or reverse.

Please see in the git repository for examples of .bed files from different
genes to see what is the correct format for the output file of your chosen
LRG xml file.

You will know the program is finished when it prints where to find the location of your results on the command line, for example:
`Your results are found in the LRG_1_COL1A1_GRCh37_19-01-15-15-10.bed file`

<h2>Example output</h2>

```

chr15      25650653        25650608        1       -
chr15      25620910        25620612        2       -
chr15      25616959        25615713        3       -
chr15      25605674        25605530        4       -
chr15      25602043        25601838        5       -
chr15      25601203        25601039        6       -
chr15      25599830        25599675        7       -
chr15      25599573        25599500        8       -
chr15      25585375        25585232        9       -
chr15      25584404        25582396        10      -

```

<h2>Troubleshooting</h2>
When you try and run our program with your chosen LRG, you may receive
either of two messages:

`ERROR: This file does not exist in this directory
Please make sure your file is saved in groupwork_lrg directory`

This error message comes up if you have not saved your LRG.xml file in the same
directory as the one from the Github directory. Please try to move your
chosen LRG.xml file into the groupwork_lrg folder.


`ERROR: Invalid file type. File must have extension .xml`

This error message comes up if the file that you are trying to use the program
with is not a .xml file, for example if you try and load a .fasta file instead.
Please download the .xml file for your chosen LRG and save it in the same
directory as the one from Github named groupwork_lrg

<h2>Testing</h2>

Run test file using pytest version 4.1.1

`pip install -U pytest`

`pytest test_exon_coordinates_finder.py`
