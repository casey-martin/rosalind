# -*- coding: utf-8 -*-
"""
Created on Wed Apr 27 17:31:07 2016

@author: martincg
"""

with open('rosalind_ba4c.txt', 'r') as myfile:
    myfile = myfile.read().strip()


def predict_spectrum(protein):
    massint = dict(zip("GASPVTCILNDKQEMHFRYW", [51, 71, 87, 97, 99, 101, 103, 
            113, 113, 114, 115, 128, 128, 129, 131, 137, 147, 156, 163, 186]))
                                                
    return [massint[i] for i in protein]
        
    
def cyclic_substr(protein):
    aa_str = []

    for i in range(len(protein)):
        for j in range(1, len(protein)):
            if i + j <= len(protein):
                aa_str.append(protein[i:(i + j)])
            else:
                aa_str.append(protein[i:] + protein[:(i + j - len(protein))])

    return(aa_str)                                                 

def cyclic_spectrum(protein):
    mass_list = [sum(predict_spectrum(i)) for i in cyclic_substr(protein)]
    
    mass_list.extend((0, sum(predict_spectrum(protein))))
    
    return mass_list
        

print ' '.join(map(str, cyclic_spectrum(myfile)))