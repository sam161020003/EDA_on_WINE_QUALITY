#output feature is quality

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('winequality-red.csv')

#summary of datatset
#print(df.info())

# Descriptive summary
# print(df.describe()) 

# shape of dataset
# print(df.shape)

#list down all the columns
#print(df.columns)

# to see different qualities of wine
#print(df['quality'].unique())

# to see sample size of each type of quality found above
# to find imbalanced dataset
#print(df['quality'].value_counts())
#conclusion is it is imbalanced dataset

# to find missing values
# print(df.isnull().sum()) 
# no missing values are present

# to see duplicate records in dataset
# jahaan true vo duplicate hota hai
# print(df.duplicated())

# vhi record nikalna hai jp duplicated hai
# print(df[df.duplicated()])

# to remove dduplicate records
# df.drop_duplicates(inplace=True)
# check
# print (df.shape)

# to find correlation 
#   THE BELOW 2 LINES ARE USED TO DISPLAY WHOLE DATA NHI TO ... DIKHATA HAI VO
# pd.set_option('display.max_rows', None)
# pd.set_option('display.max_columns', None)
# print(df.corr())


# to display
# plt.figure(figsize=(10,6))
# sns.heatmap(df.corr(),annot=True)
# plt.show()

# to display another way
# df.quality.value_counts().plot(kind='bar')
# plt.show()

# to find disftribution off fixed plot
# sns.histplot(df['fixed acidity'])
# plt.show()

# for i in df.columns:
#     sns.histplot(df[i],kde=True)
#     plt.show()

# categorical plot
# box plot bna rhe hai taki outliers bhi dekh paye
# sns.catplot(x='quality',y='alcohol',data=df,kind='box')
# plt.show()

# for scatter plot
# sns.scatterplot(x='alcohol',y='pH', hue='quality', data=df)
# plt.show()
 
