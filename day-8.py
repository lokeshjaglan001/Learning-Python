import pandas as pd

df = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]] , columns=["A","B","C"] , index = ["X","Y","Z"])

print(df.head())#Returns the first n rows of the DataFrame
print(df.tail())#Returns the last n rows of the DataFrame
print(df.columns)#Lists all column names
print(df.dtypes)#Displays data types of each column
print(df.info())#Displays a summary of the DataFrame, including the number of non-null values and data types
print(df.describe())#Provides summary statistics for numeric columns
print(df.shape)#Returns the number of rows and columns in the DataFrame as a tuple
print(df["A"].unique)
print(df.isnull())#Returns a DataFrame with True for null values and False otherwise
print(df.isnull().sum())#Counts the number of null values in each column

Ab = pd.DataFrame({
'Class 10th':['Pankaj s/o jaydeep','Jagreet s/o Joginder','Yash s/o Balwan','Nitin s/o Manish'],

'Class 11th':['Aaditya s/o Bijender','Ajay s/o Satish','Lakshay s/o Mahender','Vinay s/o Ashok'],

'Class 12th':['Aman s/o Surrender','Suresh s/o Jaypal','Kunal s/o Lilu ','Humanshu s/o Sunil Jaglan']})

print(Ab.head())