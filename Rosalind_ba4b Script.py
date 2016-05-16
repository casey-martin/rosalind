# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 14:00:35 2016

@author: martincg
"""
class protein:

    def __init__(self, dna, frame, positive_sense):
        'input True if string should be read from left to right'
        self.dna  = dna
        self.frame = frame
        self.positive_sense = positive_sense
        complement = dict(zip('ACGT', 'TGCA'))
        self.template = ""
        if self.positive_sense == False:
            for i in self.dna[::-1]:
                self.template += complement[i]
        else:
            self.template = self.dna

    
    def translate(self):
        codon = {"TTT": "F", "CTT": "L", "ATT": "I", "GTT": "V",
            "TTC": "F", "CTC": "L", "ATC": "I", "GTC": "V",
            "TTA": "L", "CTA": "L", "ATA": "I", "GTA": "V",
            "TTG": "L", "CTG": "L", "ATG": "M", "GTG": "V",
            "TCT": "S", "CCT": "P", "ACT": "T", "GCT": "A",
            "TCC": "S", "CCC": "P", "ACC": "T", "GCC": "A",
            "TCA": "S", "CCA": "P", "ACA": "T", "GCA": "A",
            "TCG": "S", "CCG": "P", "ACG": "T", "GCG": "A",
            "TAT": "Y", "CAT": "H", "AAT": "N", "GAT": "D",
            "TAC": "Y", "CAC": "H", "AAC": "N", "GAC": "D",
            "TAA": "*", "CAA": "Q", "AAA": "K", "GAA": "E",
            "TAG": "*", "CAG": "Q", "AAG": "K", "GAG": "E",
            "TGT": "C", "CGT": "R", "AGT": "S", "GGT": "G",
            "TGC": "C", "CGC": "R", "AGC": "S", "GGC": "G",
            "TGA": "*", "CGA": "R", "AGA": "R", "GGA": "G",
            "TGG": "W", "CGG": "R", "AGG": "R", "GGG": "G"}
                 
        self.aminoacid = ""
        for i in range(self.frame, len(self.template), 3):
            if (i + 3) > len(self.template):
                break
            else:
                self.aminoacid += (codon[self.template[i:i+3]])
        
        return self.aminoacid
    
    
    def motifSearch(self, motif):
        import re
        motif = re.compile(motif) 
        self.motifLocations = []
        
        for i in motif.finditer(self.translate()):
            self.motifLocations.append(i.start())
            
        return self.motifLocations
        
        
    def dnaIndex(self, motif):
        self.dnaIndices = []
        
        def revcomp(dna):
            complement = dict(zip('ACGT', 'TGCA'))
            return "".join(complement[i] for i in reversed(dna))
        
        if self.motifSearch(motif) != []:
            for i in self.motifSearch(motif):
                self.dnaIndices.append(
                self.template[(3 * i + self.frame)
                :(3 * i + (3 * len(motif) + self.frame))])
        
        if self.positive_sense == True and self.dnaIndices != []:
            return [i for i in self.dnaIndices]
        if self.positive_sense == False and self.dnaIndices != []:
            return [revcomp(i) for i in self.dnaIndices]
               
                   
            
        

with open('rosalind_ba4b(1).txt', 'r') as myfile:
    myfile = myfile.read().split()
    

for i in range(3):
    for j in (True, False):
        output = (protein(myfile[0], i, j).dnaIndex(myfile[1]))
        if output != None:
            for k in output:
                print k
        


