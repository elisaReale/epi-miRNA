#!/usr/bin/env Rscript
#prende un file senza header come pvalue_low_blahblah e aggiunge alla fine una colonna con il pvalue aggiustato per benjamini-hochbergdata$BH = p.adjust(data$V7, method = "BH")
#args[1] il file in cui aggiustare il pvalue
#args[2] il nome del file in cui salvare

#output 
#       1 gseaset
#       2 mirna
#       3 num_geni_gsea
#       4 num_geni_mirna
#       5 num_geni_universo
#       6 num_geni_intersezione
#       7 pvalue
#       8 pvalue benjamini
#       9 intersection
      
args = commandArgs(trailingOnly=TRUE)
data <-read.table(file = args[1], skip = 2, sep = "\t", header = FALSE)
data = data[order(data$V7),]
data$BH = p.adjust(data$V7, method = "BH")
write.table(data[,c(1,2,3,4,5,6,7,9,8)], file=args[2], row.names=FALSE, col.names = FALSE, sep = "\t")