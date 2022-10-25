### R script used to run one-way ANOVA between populations in Figure 1A.

## Within Population Datasets
w_FR <- c(0.968, 0.772, 0.775)
w_ZI <- c(0.787, 0.842, 0.643)
w_EF <- c(1.093, 0.978, 0.873)
w_CO <- c(0.806, 0.880, 0.883)

## Between Population Datasets, maternal first
CO_ZI <- c(0.984, 0.899,0.675)
ZI_CO <- c(0.739, 0.908,0.896)
FR_ZI <- c(0.931, 0.820, 0.887)
ZI_FR <- c(0.784, 0.988, 0.944)
EF_ZI <- c(0.745, 0.848, 0.735)
ZI_EF <- c(0.913, 0.687, 0.695)
FR_CO <- c(0.879, 1.01, 1.00)
CO_FR <- c(0.860, 0.793, 1.06)
FR_EF <- c(0.983, 0.986, 1.06)
EF_FR <- c(0.852, 0.817, 0.718)
CO_EF <- c(1.268, 0.742, 0.753)
EF_CO <- c(0.710, 0.838, 0.753)

### Example analysis between EF and CO (complete for each cross pair)
## Combined within/between groups
within <- c(w_CO, w_EF)
between <- c(CO_EF, EF_CO)
group <- gl(2, 6, 12, labels= c('within', 'between'))
tester <- c(within, between)
model <- lm(tester ~ group)
anova(model)

## For Cross direction difference test
cross_dir <- gl(2, 3, 6, labels=c('first', 'second'))
tester_2 <- c(CO_EF, EF_CO)
model_2 <- lm(tester_2 ~ cross_dir)
anova(model_2)

## single cross direction against combined within population
dir <- factor(c('within','within','within','within','within','within','between','between','between'))
within_2 <- c(w_EF, w_FR)
tester_3 <- c(within_2, FR_EF)
model_3 <- lm(tester_3 ~ dir)
anova(model_3)
