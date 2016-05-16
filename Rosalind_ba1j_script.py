# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:07:54 2016

@author: martincg
"""
with open('bahi.txt', 'r') as myfile:
    myfile = myfile.read().split()
    myfile[1:] = map(int, myfile[1:])


class nucleic_acid:
    
    def __init__(self, nuctide):
        self.nuctide = nuctide
    
    def comp(self, seq):
        return "".join([dict(zip('ACGT', 'TGCA'))[i] for i in seq])[::-1]
    
    def hamming_dist(self, st1, st2):
        assert len(st1) == len(st2)
        dist = 0
        for i in range(len(st1)):
            if st1[i] != st2[i]:
                dist += 1
        return dist
        
        
    def kmers(self, kmer):
        from collections import defaultdict
        mykmers = defaultdict(int)
        for i in range(len(self.nuctide) - kmer + 1):
            mykmers[self.nuctide[i:i+kmer]] += 1
        return mykmers
        
        
    def freq_mismatch(self, kmer, mismatch):
        from collections import defaultdict
        mymatches = defaultdict(int)
        for i in kmers(self.nuctide, kmer).keys():
            for j in range(len(self.nuctide) - kmer + 1) :
                if (hamming_dist(i, self.nuctide[j:j+kmer]) <= mismatch or 
                    hamming_dist(self.comp(i), self.nuctide[j:j+kmer]) <= mismatch):
                    mymatches[i] += 1
        return mymatches
        #return [i for i in mymatches.keys()
         #       if mymatches[i] == mymatches[max(mymatches, key = mymatches.get)]]




 




def comp(dna):
    return "".join([dict(zip('ACGT', 'TGCA'))[i] for i in dna])[::-1]
    
for i in nucleic_acid(myfile[0]).kmers(4):
    print nucleic_acid(myfile[0]).comp(i), i


foo = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'



nucleic_acid(foo).freq_mismatch(4, 1)
