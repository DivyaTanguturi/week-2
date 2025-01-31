import pandas as pd
import numpy as np
import seaborn as sns

#Load the dataset
df=pd.read_csv('C:/Users/geeth/OneDrive/Desktop/predicting Solar power output/solarpowergeneration.csv')

#Display the first few rows of the dataset
df.head()
df.tail()
df.head(10)

#to check the total number of rows and columns
df.shape

#Display summary
df.describe()

#check the information of the dataset
df.info()

#Check for the missing values
df.isnull().sum()

#Check dulpicate values
df.duplicated().sum()

import matplotlib.pyplot as plt
#plot distibution of power
plt.figure(figsize=(10,6))
sns.histplot(df['generated_power_kw'],bins=30,kde=True)
plt.title('Distribution of Generated Power(kW)')
plt.xlabel('Generated Power(kW)')
plt.ylabel('Frequency')
plt.show()

df[df.columns[:9]].hist(bins=30,figsize=(15,10))
plt.show()

df[df.columns[9:18]].hist(bins=30,figsize=(15,10))
plt.show()

df[df.columns[18:21]].hist(bins=30,figsize=(15,10))
plt.show()

df[df.columns[18:20]].hist(bins=30,figsize=(6,4))
plt.show()

#Bivarite analysis
#Scatter plot with target feature
plt.figure(figsize=(15,30))
for i,column in enumerate(df.columns):
    plt.subplt(7,3,i+1)
    plt.scatter(df[column],df['generated_power_kw'])
    plt.title(f'{column} vs Generated Power(KW)')
    plt.xlabel(column)
    plt.ylabel('Generated power(kw)')
plt.tight_layout()
plt.show()

df.corr()

plt.figure(figsize=(15,10))
sns.heatmap(df.corr(),cmap='coolwarm',annot=True,fmt='.2f')

#outlier
plt.figure(figsize=(15,30))
for i,column in enumerate(df.columns):
    plt.subplot(7,3,i+1)
    sns.boxplot(df[column])
plt.show()


















