library("seqinr")

#function for readling a list of fasta urls in an lapply function
fasta.list <- function(x) {
  read.fasta(x, as.string = T, set.attributes = F)
}
#function that returns location of glycosylation motif. the ?= enables identification of overlapping motif sites
motif.search <- function(x){
  gregexpr(pattern = "(?=[n][^p][st][^p])", x, perl = T, ignore.case = T)
}

#load table of accession numbers
AC.numbers <- (as.matrix(read.table("rosalind_mprt.txt")))

#creates the uniprot url for each accession number
fasta.urls <- paste("http://www.uniprot.org/uniprot/", AC.numbers, ".fasta", sep = "")


#opens Uniprot URL for each AC and reads sequence data as fasta
AC.list <- lapply(fasta.urls, fasta.list)
AC.list <- lapply(AC.list, as.character)

#searches and saves each matching motif in a matrix next to its accession number.
motif.locations <- as.matrix(lapply(AC.list, motif.search))
motif.locations <- data.frame(AC.numbers, motif.locations)

print(motif.locations)
