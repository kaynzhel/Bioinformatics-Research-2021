'''
Author: Kaye Ena Crayzhel F. Misay
Date Created: May 14, 2021
Date Last Edited: June 01, 2021

This code only prints out the Accession ID and the Sequence from the fasta file.
From here, you can change the code to accommodate with your needs.

References:
Biopython Documentation
'''

from Bio import SeqIO
import csv, argparse

def main():
    file_name = getFileName()
    # transforms the fasta file to a csv file with headers accession and its sequence
    dot_index = file_name.index('.')
    with open(file_name[:dot_index] + '.csv', mode='w') as csv_file:
        field_names = ['Accession ID', 'Sequence'] # header
        writer = csv.DictWriter(csv_file, fieldnames=field_names)
        writer.writeheader()
        for seq_record in SeqIO.parse(file_name, "fasta"): # parser
            row = {'Accession ID': seq_record.id, 'Sequence': seq_record.seq}
            writer.writerow(row)

def getFileName():
    # command line argument
    description = 'Give the file name of the converted csv file.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
    return args.file_name

main()