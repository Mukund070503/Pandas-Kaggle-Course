import pandas as pd

#pandas have 2 objects DataFrame and Series
#DataFrame are tables with an array of entities. Each entities have values.
#Series is a collection of values like a list. It has only one column and it does not have a column name it can only have an overall name

pd.DataFrame({'Name':["Mukund","Madhav"],'Score':[80,75]},index=[1,2])  #index is not compulsory but in case of default it will start from 0, it can also be string

pd.Series([10,20,30], index=['value1','value2','value3'],name='Points') #Here index and name is not compulsory in default case index will start with 0

dataSet = pd.read_csv("Path") #This has over 30 parameters that can be specified for Example if data set has in-built index column
#we need to specify that otherwise a new col will be created like this dataSet = pd.read_csv("Path",index_col=0)

dataSet.shape
dataSet.head()#Top 5 rows, you can also add a value in () specifying how many rows you want
dataSet.tail()#Last 5 rows
dataSet.to_csv('name') # to create a csv file and save it 


pd.set_option('display.max_rows', 5) ##if we want to set display to show only 5 rows 


classroom = pd.DataFrame({'Name':["Mukund","Madhav","Atharv","Yug","Vasu"],'Roll_No':[1,2,3,4,5]},index=[3,4,5,6,7])

classroom.Roll_No / classroom['Roll_No'] # These are the 2 ways to access the attributes of a table entire column

classroom['Name'][3] #will give Mukund 

#index based selection (iloc)

classroom.iloc[0] # will give the first row of object 

classroom.iloc[0:2] # will give first and second row of object 

classroom.iloc[0:2,0] #will give first and second row of object and also only first col

classroom.iloc[[1,3,4],0] #will give rows with index 1,3,4 and in that also just their names that is col 1 with index 0

#Label based Selection (loc)

classroom.loc[3] # will give the first row as output 

classroom.loc[3:5,"Name"] # will give output as first and second rows with Name col 

#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded.
#So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.

classroom = classroom.set_index("Roll_No") # will make roll no col as index 

classroom.Name == 'Mukund'  #To get a col with first row as True all others as false

##Conditional selection

classroom.loc[classroom.Name == 'Mukund']

classroom.loc[(classroom.Name == 'Mukund')&(classroom['Roll_No']==1)]

classroom.loc[(classroom.Name == 'Mukund')|(classroom["Roll_No"]==3)]

classroom.loc[classroom.Name.isin(['Mukund', 'Atharv'])]

classroom.loc[classroom.Name.notnull()]  # similarly we can use isnull() as well

#Assigning Value

classroom["Roll_No"]=range(4,len(classroom)+4) 

# Summary Functions and Maps

classroom["Roll_No"].describe()

classroom["Roll_No"].mean()

classroom["Roll_No"].unique()

classroom["Roll_No"].value_counts()

mean_to_subtract = classroom["Roll_No"].mean()

#map()






