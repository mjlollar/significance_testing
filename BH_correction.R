setwd("~/Desktop/final_pvalues_062022/grid/")
data <- read.csv("5x5_individual_cross_50_pvalues_041022.csv", header=T, as.is=T)

cross <- c(data$cross)
rawp <- c(data$p_value)

# Methods: "holm", "hochberg", "hommel", "bonferroni", "BH", "BY", "fdr", "none")

#Benjamini-Hochberg
out_BH <- p.adjust(rawp,method="BH")
df_out_BH <- data.frame(cross=cross, BH_adjusted_P=out_BH)
write.csv(df_out_BH,"BH_adjusted.csv", row.names=F)

#Bonferroni
out_bonferroni <- p.adjust(rawp,method="bonferroni")
df_out_bonferroni <- data.frame(cross=cross, bonferroni_adjusted_P=out_bonferroni)
write.csv(df_out_bonferroni,"bonferroni_adjusted.csv", row.names=F)
