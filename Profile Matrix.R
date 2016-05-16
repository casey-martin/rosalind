library(seqinr)

consensus <- t(data.frame(read.fasta("rosalind_cons(1).txt", 
                                     as.string = F,  
                                     set.attributes = F)))   #imports the FASTAs into an MSA dataframe


nt.column <- apply(consensus, 2, table) #gives a list of tables of nt counts for each MSA column

nt.column <- lapply(nt.column, as.matrix) #converts the nested table of nt counts to a matrix with nt rownames

#creates a list the length of the sequences that will be filled during the for loop
n <- length(nt.column)
profile.matrix <- numeric(n)

#apply the row.names function for each max value of the nt count submatrices in the nt.column list.
  for (i in (1:n)){
    profile.matrix[i] <- row.names(nt.column[[i]])[apply(nt.column[[i]], 2, which.max)]
  }

#output the profile matrix and collapse the string
paste(profile.matrix, collapse = "")













