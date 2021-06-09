'''
Author: Kaye Ena Crayzhel F. Misay
Date Created: May 10, 2021
Date Last Edited: June 09, 2021

The code is edited for simplicity and general use.
It only prints out the Accession ID of the sequence, mutations, and mutation positions.
From here, you can change the code to accomodate with your needs.
'''
import os, csv, argparse

def main():
    file_name = getFileName()
    program = Task(file_name)
    program.run()

def getFileName():
    # command line argument
    description = 'Give the file name of the fasta file.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("file_name", type=str)
    args = parser.parse_args()
    return args.file_name

class Task:
    def __init__(self, file_name):
        self.sequence_file = file_name
        self.reference = '' # the reference sequence
        self.mutations = [] # a list of all the mutations of a given accession ID
        self.mutation_pos = [] # a list of all the mutation positions of a given accession ID
        self.row_output = {} # a dictionary of the row output for the csv file
    
    def run(self):
        # the function that runs the script
        if self.checkIfFileExists(): self.performTask()
        else: print ("File does not exist. Try again!")

    def checkIfFileExists(self):
        if os.path.isfile(self.sequence_file): return True
        else: return False
    
    def performTask(self):
        # counting the number of new mutations
        with open(self.sequence_file, mode='r') as file1, open('output_' + self.sequence_file, mode='w') as output_file:
            # writing the headers
            field_names = ['Accession ID', 'Mutations', 'Mutation Positions'] # header
            self.writer = csv.DictWriter(output_file, fieldnames=field_names)
            self.writer.writeheader()

            self.file1_read = csv.DictReader(file1) # reading the sequence file

            self.getInfo() # gather info then write to csv file

    def getInfo(self):
        # it gathers information on the input file then writes the collected data to the output_file
        self.reference = next(self.file1_read)['Sequence'] # sequence of the reference file
        
        # reading through the rows of self.sequence_file
        for row in self.file1_read:
            self.mutations, self.mutation_pos = [], []
            for index in range(len(row['Sequence'])): # runs for as long as the range of the sequence
                if self.reference[index] != row['Sequence'][index]:
                    # To collect the mutation in the form of reference amino acid + column/position + mutated amino acid
                    # example: D614G
                    self.mutations.append(self.reference[index]+str(index+1)+row['Sequence'][index])
            
            # determines the position of the mutation
            for mutation in self.mutations:
                self.mutation_pos.append(mutation[1:(len(mutation)-1)])
            
            # writing the row to the csv file
            self.row_output = {'Accession ID':row['Accession'], 'Mutations': ','.join(self.mutations), 'Mutation Positions': ','.join(self.mutation_pos)}
            self.writer.writerow(self.row_output)

if __name__ == "__main__":
   main()