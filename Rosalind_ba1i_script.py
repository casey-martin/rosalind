# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:07:54 2016

@author: martincg
"""
with open('rosalind_ba1h.txt', 'r') as myfile:
    myfile = myfile.read().split()


foo = 'ACGTTGCATGTCGCATGATGCATGAGAGCT'


class nucleic_acid:
    
    def __init__(self, nuctide):
        self.nuctide = nuctide
    
def hamming_dist(st1, st2):
    dist = 0
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            dist += 1
    return dist
    
    
def kmers(nuctide, kmer):
    from collections import defaultdict
    mykmers = defaultdict(int)
    for i in range(len(nuctide) - kmer + 1):
        mykmers[nuctide[i:i+kmer]] += 1
    return mykmers
    
    
def freq_mismatch(nuctide, kmer, mismatch):
    from collections import defaultdict
    mymatches = defaultdict(int)
    for i in kmers(nuctide, kmer).keys():
        for j in range(len(nuctide) - kmer + 1) :
            if hamming_dist(i, nuctide[j:j+kmer]) <= mismatch:
                mymatches[i] += 1               
    return [i for i in mymatches.keys()
            if mymatches[i] == mymatches[max(mymatches, key = mymatches.get)]]

freq_mismatch(foo, 4, 1)




foo = dict(zip('ACGT', [5, 9, 3, 4]))

max(foo, key = foo.get)














