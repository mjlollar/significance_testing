library("EnvStats")
library("tidyverse")

setwd("/home/matt/song_secondpass/R_work/inbred")
df <- read.csv("inbred_filtered_mean_061523_subset.csv", header=T, as.is=T) #filtered data

pvalues <- vector("logical",10000) #Initiate p.value list

#calculate Mann-Whitney for each trait
for (x in (1:10000)){
  
  #Shuffle line population identity
  df.shuffle <- transform(df, population = sample(population))
  df.shuffle$population <- as.factor(df.shuffle$population)
  
  # Calculate M.W. for each test
  p.value.tmp <- vector("logical",29)
  i=1
  for (y in (2:30)){
    col.name <- colnames(df.shuffle)[y]
    df_fr <- df.shuffle %>% filter(population=='FR') %>% select(all_of(col.name))
    df_fr <- dplyr::pull(df_fr, col.name)
    df_zi <- df.shuffle %>% filter(population=='ZI') %>% select(all_of(col.name))
    df_zi <- dplyr::pull(df_zi, col.name)
    test.mw <- wilcox.test(x=df_fr, y=df_zi, paired=FALSE, na.rm=T)
    p.value.tmp[i] <- test.mw$p.value
    i = i + 1
    rm(col.name, df_fr, df_zi, test.mw)
  }
  
  #Get minimum p.value for replicate tests
  min.pvalue <- min(p.value.tmp)
  pvalues[x] <- min.pvalue
  print(x)
  rm(df.shuffle, i, p.value.tmp)
}

#sort pvalues, get pvalue @ alpha=0.05, print to output
pvalues <- sort(pvalues)
print(pvalues[500])
write.csv(pvalues, file="MW_multipletest_perm_pvalues_061623.csv", row.names=FALSE)
