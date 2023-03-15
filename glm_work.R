# Base model
df <- read.csv('glm_input.csv', header=T, as.is=T) #load dataframe

df$maternal <- as.factor(df$maternal) 
df$paternal <- as.factor(df$paternal)
df$type <- as.factor(df$type)

glm.base <- glm(family="quasibinomial",formula=status ~ type, data=df)
summary(glm.base)

#GLM dummy reference category, Model 2
df_dummy <- read.csv('glm_input_dummy.csv', header=T, as.is=T)

df_dummy$maternal <- as.factor(df_dummy$maternal) 
df_dummy$paternal <- as.factor(df_dummy$paternal)
df_dummy$type <- as.factor(df_dummy$type)

df_dummy$maternal <- relevel(df_dummy$maternal, ref='AM')
df_dummy$paternal <-relevel(df_dummy$paternal, ref='AP')

glm.model2.dummy <- glm(family="quasibinomial", formula=status ~ type + maternal + paternal, data=df_dummy)
summary(glm.model2.dummy)

#GLM closest strain to mean as reference category, Model 2
group_maternal <- aggregate(df$status,list(df$maternal),mean) #maternal mean of each strain
group_paternal <- aggregate(df$status,list(df$paternal),mean) #paternal mean of each strain
m <- mean(group_maternal$x) #list of maternal means in index order below
p <- mean(group_paternal$x) #list of paternal means in index order below
m_diff <- abs(group_maternal$x - m) #list of the difference in strain mean and population mean
p_diff <- abs(group_paternal$x - p)
which.min(m_diff) #get index of lowest difference
# 8, Z3 (ZI366N) 
which.min(p_diff) 
# 8, Z3 (ZI366N)

# index position coords
# 1  2  3  4  5  6   7  8  9  10
# f1 f2 f3 f4 f5 zi1 z2 z3 z4 z5 

which.min(m_diff) # 8, Z3
which.min(p_diff) # 8, Z3

df$maternal <- relevel(df$maternal, ref='Z3')
df$paternal <- relevel(df$paternal, ref='Z3')

glm.model2.closest <- glm(family="quasibinomial", formula=status ~ type + maternal + paternal, data=df)
summary(glm.model2.closest)
