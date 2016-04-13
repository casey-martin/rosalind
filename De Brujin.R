library(seqinr)

dna <- (readLines("rosalind_dbru.txt"))

complement <- function(x){
  comp <- c(A = "T", C = "G", G = "C", T = "A")
  return(comp[x])
}

dna <- unique(c(unlist(lapply(dna, function(x){(paste(rev(complement(s2c(x))), collapse = ""))})), dna))

revkmers <- data.frame()

kmers <- data.frame()
for (i in 1:length(dna)){
  kmers[i,1] <- substr(dna[i], 1, nchar(dna)-1)
  kmers[i,2] <- substr(dna[i], 2, nchar(dna))
}


output <- apply(kmers, 1, function(x){paste(x, collapse = ", ")})
output <- as.matrix(lapply(output, function(x){paste("(", x, ")", sep = "")}))

write.table(output, "dbru.txt", quote = FALSE, row.names = FALSE, col.names = FALSE)

