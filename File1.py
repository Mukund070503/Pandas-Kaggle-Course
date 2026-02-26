import pandas as pd

#pandas have 2 objects DataFrame and Series
#DataFrame are tables with an array of entities. Each entities have values.
#Series is a collection of values like a list. It has only one column and it does not have a column name it can only have an overall name

pd.DataFrame({'Name':["Mukund","Madhav"],'Score':[80,75]},index=[1,2])  #index is not compulsory but in case of default it will start from 0, it can also be string
