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
                self.aminoacid = self.aminoacid + (codon[self.template[i:i+3]])
        
        return self.aminoacid
        
        

                    
myseq = "TTCCTTATTGTT"

forward_sense = []

for i in range(3):
     forward_sense.append(protein(myseq, i, True).translate())

print protein(myseq, 1, True).translate()