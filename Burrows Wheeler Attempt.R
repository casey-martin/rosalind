dna <- "GCGTGCCTGGTCA"

bwt <- function(x){
  x <- paste0(x, "?")
  lex_order <- order(substring(x, 1:nchar(x), nchar(x)))
  bwt <- c()
  for (i in lex_order){
    if (i == 1){
      bwt <- append(bwt, "$")
    } else {
      bwt <- append(bwt, substring(x, i-1, i-1))
    }
  }
  return(data.frame(bwt, lex_order))
}

paste(bwt(dna)$bwt, collapse = "")




dna1 <- readLines("rosalind_ba9g.txt")

suffix.array <- function(x){
  lex_order <- order(substring(x, 1:nchar(x), nchar(x)))
  return(lex_order - 1)
}

write.table(suffix.array(dna1))
