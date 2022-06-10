# Bioinformatics-Research-2021
This is a repository containing some of the scripts (general ones) I wrote during a four-month research on Sars-CoV-2 and the Influenza Virus in the University of Alberta.

## fasta2csv.py
### DESCRIPTION:
This is a script that converts a fasta file into a CSV file. 
It needs a command line input of the name of the FASTA file that needs to be converted.
It has an output with two columns: Accession ID and its sequence.
These outputs can be changed by re-writing lines 17 and 21.

### HOW TO RUN:
python3 fasta2csv.py fasta_file_name

## getMutations.py
### DESCRIPTION:
This is located in the getMutations folder.
It is a script that generates the mutations and mutation positions of all the sequences given a reference sequence.
The reference sequence must be at the first row of the input CSV file; otherwise, you may change the code.
It has an output with three columns: Accession ID, mutations, and mutation positions.
These output can be changed by re-writing lines 46 and 72, with additional lines for the added information, if needed.

Example input and output are provided in the getMutations folder as well.

### HOW TO RUN:
python3 getMutations.py csv_file_name
