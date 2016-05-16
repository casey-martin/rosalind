# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 17:07:54 2016

@author: martincg
"""
with open('rosalind_ba1h.txt', 'r') as myfile:
    myfile = myfile.read().split()

def hamming_dist(st1, st2):
    dist = 0
    for i in range(len(st1)):
        if st1[i] != st2[i]:
            dist += 1
    return dist
    
def approx_match(st1, st2, d): 
    locations = []    
    for i in range(len(st2)-len(st1)):
        if hamming_dist(st1, st2[i:i+len(st1)]) <= int(d):
            locations.append(i)
    return locations
    
print ' '.join(map(str, approx_match(myfile[0], myfile[1], myfile[2])))