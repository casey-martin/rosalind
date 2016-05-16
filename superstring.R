####Slow but works


library(seqinr)

myseqs <- read.fasta("rosalind_long.txt", set.attributes = F, as.string = T)

superstring <- myseqs[3]
myseqs <- myseqs[-3]
x <- 1

while(length(myseqs) > 0){
 ##5' superstring check
  for (i in 2:(nchar(myseqs[x])/2)){
    small.overlap.3 <- substr(myseqs[x], i, nchar(myseqs[x]))
    l <- nchar(small.overlap.3)
    super.overlap.5 <- substr(superstring, 1, l)
    if (small.overlap.3 == super.overlap.5){
      print(paste("I found a 5' SS match at", names(myseqs[x])))
      superstring <- paste(myseqs[x], substr(superstring, l+1, nchar(superstring)), sep = "")
      myseqs <- myseqs[-x]
      break
    }
  }
  
 ##3' superstring check
  for (i in 1:((nchar(myseqs[x])/2)-1)){
    small.overlap.5 <- substr(myseqs[x], 1, nchar(myseqs[x])-i)
    l <- nchar(small.overlap.5)
    super.overlap.3 <- substr(superstring, nchar(superstring)-l+1, nchar(superstring))
    if (small.overlap.5 == super.overlap.3){
      print(paste("I found a 3' SS match at", names(myseqs[x])))
      superstring <- paste(superstring, substr(myseqs[x], nchar(myseqs[x])-i+1, nchar(myseqs[x])), sep = "")
      myseqs <- myseqs[-x]
      break
    }
  }
 
 #increase counter. If counter increases beyond current list length, reset to 1 
  x <- x + 1
  if (x > length(myseqs)){
    x <- 1
    print(paste("String Length:", nchar(superstring)))
  }
}

