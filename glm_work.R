#GLM dummy model
df_dummy <- read.csv('glm_input_dummy_0323.csv', header=T, as.is=T)

df_dummy$maternal <- as.factor(df_dummy$maternal) 
df_dummy$paternal <- as.factor(df_dummy$paternal)
df_dummy$type <- as.factor(df_dummy$type)

df_dummy$maternal <- relevel(df_dummy$maternal, ref='AM')
df_dummy$paternal <-relevel(df_dummy$paternal, ref='AP')

glm.1 <- glm(family="quasibinomial", formula=status ~ type + maternal + paternal, data=df_dummy)
summary(glm.1)

#GLM closest strain to mean
df <- read.csv('glm_input_010923.csv', header=T, as.is=T) #load dataframe

df$maternal <- as.factor(df$maternal) 
df$paternal <- as.factor(df$paternal)
df$type <- as.factor(df$type)

group_maternal <- aggregate(df$status,list(df$maternal),mean)
group_paternal <- aggregate(df$status,list(df$paternal),mean)
m <- mean(group_maternal$x)
p <- mean(group_paternal$x)
m_diff <- abs(group_maternal$x - m)
p_diff <- abs(group_paternal$x - p)
which.min(m_diff) # 8, Z2
which.min(p_diff) # 8, Z2

# index position coords
# 1  2  3  4  5  6   7  8  9  10
# f1 f2 f3 f4 f5 zi1 z2 z3 z4 z5 

which.min(m_diff) # 8, Z2
which.min(p_diff) # 8, Z2

df$maternal <- relevel(df$maternal, ref='Z2')
df$paternal <- relevel(df$paternal, ref='Z2')

glm.2 <- glm(family="quasibinomial", formula=status ~ type + maternal + paternal, data=df)
summary(glm.2)
