library(seqinr)

options(digits = 5)

mydat <- (lapply(read.fasta("rosalind_pdst.txt", seqonly = TRUE,), s2c))

alldat <- expand.grid(mydat, mydat)

dist_check <- function(x){
  return(sum(x[1, 1][[1]] != x[1, 2][[1]])/length(x[1, 1][[1]]))
}

dist_mat <- list()

for (i in 1:nrow(alldat)){
  dist_mat[i] <- dist_check(alldat[i, ])
}

dist_mat <- apply(matrix(unlist(dist_mat), nrow = length(mydat)), 1, function(x){format(x, nsmall = 5)})

write.table(dist_mat, "pdst_output.txt", row.names = FALSE, col.names = FALSE, quote = FALSE)
