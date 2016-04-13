import os
import re

#Sets working directory
os.chdir("\Users\martincg\Downloads")

myfile = open("./rosalind_ba1f(1).txt", "r")
genome = myfile.read()

skew = [0]

for i in range(len(genome)): 
    if genome[i] == "C":
        skew.append(skew[i]-1)
    if genome[i] == "G":
        skew.append(skew[i]+1)
    if genome[i] == "T" or genome[i] == "A":
        skew.append(skew[i])
    
for i in range(len(skew)):
    if skew[i] == min(skew):
        print i


