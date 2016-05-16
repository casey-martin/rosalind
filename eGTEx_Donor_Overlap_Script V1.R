library(xlsx)

setwd("/Users/martincg/Documents/GTEx/eGTEx Shipments")
wd_files <- list.files()

all_data <- lapply(wd_files, function(x){read.xlsx(x, 1)})

donors <- c()

#Converts data in excel from factor to character
for (i in seq_along(all_data)){
  donors <- c(donors, as.character(all_data[[i]]$Participant.ID.s.))
}

#Lexicographical order of all unique donors
donors <- na.omit(sort(unique(donors)))

#list of unique donors for each PI
PI_list <- c()
for (i in seq_along(all_data)){
  PI_list[[i]] <- unique(na.omit(as.character(all_data[[i]]$Participant.ID.s.)))
}


locations <- lapply(PI_list, function(x){
  sapply(x, function(y){grep(y, donors)})})

names(locations) <- wd_files

overlap <- matrix(0, nrow = length(donors), ncol = length(wd_files))


for (i in seq_along(locations)){
  overlap[locations[[i]], i] <- 1
}

rownames(overlap) <- donors
colnames(overlap) <- gsub(".xlsx", "", wd_files)


write.xlsx(overlap, "eGTEx donor overlap V1.2.xlsx")


