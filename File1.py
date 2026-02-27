import pandas as pd

#pandas have 2 objects DataFrame and Series
#DataFrame are tables with an array of entities. Each entities have values.
#Series is a collection of values like a list. It has only one column and it does not have a column name it can only have an overall name

pd.DataFrame({'Name':["Mukund","Madhav"],'Score':[80,75]},index=[1,2])  #index is not compulsory but in case of default it will start from 0, it can also be string

pd.Series([10,20,30], index=['value1','value2','value3'],name='Points') #Here index and name is not compulsory in default case index will start with 0

dataSet = pd.read_csv("Path") #This has over 30 parameters that can be specified for Example if data set has in-built index column
#we need to specify that otherwise a new col will be created like this dataSet = pd.read_csv("Path",index_col=0)

dataSet.shape
dataSet.head()
dataSet.to_csv('name') # to create a csv file and save it 
