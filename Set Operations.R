#data import and clean up
mydat <- readLines("rosalind_seto(3).txt")
mydat <- gsub("[{}]", "", mydat)
mydat <- lapply(mydat, function(x){(strsplit(x, ","))})
mydat <- lapply(mydat, function(x){lapply(x, as.numeric)})
mydat <- lapply(mydat, unlist)

rosalind_format <- function(x){
  out <- gsub("[c()]", "", paste(x, collapse = ", "))
  return(gsub("\n", "", paste("{", out, "}", sep = "")))
}

write
rosalind_format(union(mydat[2], mydat[3]))
rosalind_format(intersect(mydat[[2]], mydat[[3]]))
rosalind_format(setdiff(mydat[2], mydat[3]))
rosalind_format(setdiff(mydat[3], mydat[2]))
rosalind_format(setdiff(1:mydat[[1]], mydat[2]))
rosalind_format(setdiff(1:mydat[[1]], mydat[3]))


