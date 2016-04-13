library(seqinr)

myseqs <- (read.fasta("rosalind_corr.txt", seqonly = TRUE))

read_counts <- lapply(myseqs, function(x){
  (grepl(paste0(x, "|", c2s(rev(comp(s2c(x))))), myseqs, perl = TRUE, ignore.case = TRUE))
})

error <- which(sapply(read_counts, sum) == 1)
error <- myseqs[error]
myseqs <- myseqs[-(which(sapply(read_counts, sum) == 1))]
myseqs <- toupper(c(myseqs, lapply(myseqs, function(x){c2s(rev(comp(s2c(x))))})))


seqcombn <- expand.grid(error, myseqs)
seqcombn <- t(apply(seqcombn, 1, as.character))

hamming.list <- mapply(function(x, y){sum(s2c(x) != s2c(y))}, seqcombn[,1], seqcombn[,2])

hamming.list <- which(hamming.list == 1)

error <- seqcombn[hamming.list,]

error <- unique(mapply(function(x, y){paste(x, "->", y, sep = "")}, error[,1], error[,2]))

write.table(error, "error_output.txt", quote = FALSE, row.names = FALSE, col.names = FALSE)



