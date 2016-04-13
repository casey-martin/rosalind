import os

complement = {'T':'A', 'A':'T', 'C':'G', 'G':'C'}
    
os.chdir("\Users\martincg\Documents")

myfile = open("./rosalind_dna.txt", "r")
myseq = myfile.read()

retval = os.getcwd()

print myseq
