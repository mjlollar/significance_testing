setwd("/Users/matt/Desktop/paper_review/glm")
df <- read.csv('glm_input_022123.csv', header=T, as.is=T)
df <-read.csv('glm_input_1_success_022123.csv',header=T, as.is=T)


library('arm')
library('magritter')
library('tidyverse')
library('dplyr')

df$maternal <- as.factor(df$maternal)
df$paternal <- as.factor(df$paternal)
df$type <- as.factor(df$type)

#Model 1
glm.fit.1 <- glm(family="quasibinomial",formula=status ~ type, data=df)
fit.1 <- summary(glm.fit.1)
display(glm.fit.1,digits=3)

#### https://www.science.smith.edu/~jcrouser/SDS293/labs/lab4-r.html
glm_prob <- data.frame(probs = predict(glm.fit.1, type="response"))
glm_pred <- glm_prob %>%
  mutate(pred=ifelse(probs>.5,"1","0"))
glm_pred = cbind(df, glm_pred)
glm_pred %>%
  count(pred, status) %>%
  spread(status, n, fill=0)
glm_pred %>%
  summarize(score=mean(pred== status)) # Prediction rate
####


#Model 2
glm.fit.2 <- glm(formula=status ~ type + maternal + paternal, data=df)
fit.2 <- summary(glm.fit.2)
display(glm.fit.2)

#### https://www.science.smith.edu/~jcrouser/SDS293/labs/lab4-r.html
glm_prob <- data.frame(probs = predict(glm.fit.2, type="response"))
glm_pred <- glm_prob %>%
  mutate(pred=ifelse(probs>.5,"1","0"))
glm_pred = cbind(df, glm_pred)
glm_pred %>%
  count(pred, status) %>%
  spread(status, n, fill=0)
glm_pred %>%
  summarize(score=mean(pred== status)) # Prediction rate
####

# Model 3
glm.fit.3 <- glm(formula=status ~ type + maternal + paternal + maternal:paternal, data=df)
fit.3 <- summary(glm.fit.3)
display(glm.fit.2.f3)
fit.2.f3
