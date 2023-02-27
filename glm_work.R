setwd("/Users/matt/Desktop/paper_review/glm")
df <- read.csv('glm_input_022123.csv', header=T, as.is=T)

library('arm')

df$maternal <- as.factor(df$maternal)
df$paternal <- as.factor(df$paternal)
df$type <- as.factor(df$type)
#df$type <-relevel(df$type, ref="0")

#Model 1
glm.fit.1 <- glm(formula=status ~ type, data=df)
fit.1 <- summary(glm.fit.1)
display(glm.fit.1,digits=3)

#Model 2
glm.fit.2 <- glm(formula=status ~ type + maternal + paternal, data=df)
fit.2 <- summary(glm.fit.2)
display(glm.fit.2)
fit.2

# Model 3
glm.fit.3 <- glm(formula=status ~ type + maternal + paternal + maternal:paternal, data=df)
fit.3 <- summary(glm.fit.3)
display(glm.fit.2.f3)
fit.2.f3
