import urllib
import re

fastalist = open("rosalind_mprt.txt", "r").read().splitlines()

def motif_search(fastalist):

    for i in range(len(fastalist)):
        fastalist[i] = fastalist[i].rstrip()
    
    myurl = "http://www.uniprot.org/uniprot/"
    protein = []
    
    for i in range(len(fastalist)):
        protein.append(urllib.urlopen(myurl + fastalist[i] + ".fasta").readlines()[1:])
    
    motif = re.compile("(?=N[^P][ST][^P])")
    
    for i in range(len(protein)):
        protein[i] = "".join(protein[i])
        protein[i] = protein[i].replace("\n", "")
    
    motif_locations = []
    
    for i in protein:
        motif_locations.append([j.start() + 1 for j in motif.finditer(i)])
    
    
    prot_motifs = dict(zip(fastalist, motif_locations))
    
    return (prot_motifs)

prot_motifs = motif_search(fastalist)


for i in prot_motifs:
    if prot_motifs[i] != []:
        print i 
        print " ".join(map(str, [j for j in prot_motifs[i]]))
