Download our repository from Github here:
https://github.com/Davidholmes1993/groupwork_lrg

For the gene you want to investigate on https://www.lrg-sequence.org/ ,
download the .xml file for that gene and save this into the same folder from
the repository from Github.

On your command line, type python exon_coordinates_finder.py
as well as the name of the LRG file that you have downloaded and saved
with a space in between the program and filename.
For example if you downloaded LRG_1,
type into the command line:
python exon_coordinates_finder.py LRG_1.xml

You will receive a message for the name of the file where your results
are stored in a .bed file, which will be found in the repository folder.
Open this file to see the information about the gene name, LRG number,
the exons and the coordinates where the exons start and end
in the LRG file.

Please see in the git repository for examples of .bed files from different
genes to see what is the correct format for the output file of your chosen
LRG xml file.

When you try and run our program with your chosen LRG, you may receive
either of two messages:

ERROR: This file does not exist in this directory
Please make sure your file is saved in groupwork_lrg directory

This error message comes up if you have not saved you LRG.xml file in the same
directory as the one from the Github directory. Please try to move your
chosen LRG.xml file into the groupwork_lrg folder.


ERROR: Invalid file type. File must have extension .xml

This error message comes up if the file that you are trying to use the program
with is not a .xml file, for example if you try and load a .fasta file instead.
Please download the .xml file for your chosen LRG and save it in the same
directory as the one from Github named groupwork_lrg
