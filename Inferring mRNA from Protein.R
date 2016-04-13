library(seqinr)

aa_string <- s2c(as.matrix(read.table("rosalind_mrna(3).txt"))) 

#Named list of codon frequency tables

codons <- c(A = 4, C = 2, D = 2, E = 2, F = 2, 
            G = 4, H = 2, I = 3, K = 2, L = 6, 
            M = 1, N = 2, P = 4, Q = 2, R = 6, 
            S = 6, T = 4, V = 4, W = 1, Y = 2)

#Calculates total number of mrna possibilities along the string. Takes modulo 1M when product >1M.
total <- 1 

for (i in aa_string){
  total <- total * (codons[i])
  if (total >= 1000000){
    total <- total %% 1000000
  }
}

#Takes stop codons into account
(total * 3) %% 1000000
