library(seqinr)

#imports fasta list and saves names as attributes
DNA.list <- as.matrix(read.fasta("rosalind_grph.txt", as.string = T, seqonly = F))


#substring functions
substrRight <- function(x){
  substr(x, nchar(x)-2, nchar(x))
}

substrLeft <- function(x){
  substr(x, 1, 3)
}


#gives every permutation of all seqs
all.combs <- expand.grid(DNA.list, DNA.list, KEEP.OUT.ATTRS = T, stringsAsFactors = T)


#creates an empty matrix to be filled during for loop
graph <- matrix(nrow = nrow(all.combs), ncol = 2)
#compares ends of the permutation matrix and returns the fasta names if match occurs
for (i in 1:nrow(all.combs)){
  if ((substrLeft(all.combs[[i, 1]]) == substrRight(all.combs[[i, 2]])) && (all.combs[[i, 1]] != all.combs[[i, 2]])) {
    graph[[i, 2]] <- (attr(all.combs[[i, 1]], "name"))
    graph[[i, 1]] <- (attr(all.combs[[i, 2]], "name"))
  }
}

#omits all non matches from graph matrix
graph <- as.data.frame(na.omit(graph))

#separates the two fasta names with by a space to satisfy the Rosalind answer format
collapse <- function(x){
  paste(x, collapse = " ")
}
graph.space <- apply(graph, 1, collapse)

#spits out a table for further cleanup for submission
write.table(graph.space, file = "overlap_graphs_final.txt")
  