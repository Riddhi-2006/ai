import pandas as pd

series = pd.Series([1,2,3,4,5], index = ['first','sec','third','four','fifth'] , name = 'name')
print(series)
onco = pd.read_csv("C:/Users/riddh/Downloads/oncologists_nyc.csv",index_col = 0)
# print(onco)
# print(onco.shape)
# print(onco.head())
# print(onco.name)
# print(onco.columns)
# print(onco['phone'])
# print(onco.iloc[:,0])
# print(onco.iloc[1]['name'])
# print(onco.iloc[0])
# print(onco.iloc[:,0])
# print(onco.iloc[:3,0])
# print(onco.loc['ChIJlZ4P8qb3wokRwmH1-7F0TEM','name'])
# onco = onco.reset_index()
# print(onco.loc[0,'name']) 
# print(onco.loc[:3,['street','phone','state']])#iloc uses the Python stdlib indexing scheme, where the first element of the range is included and the last one excluded. So 0:10 will select entries 0,...,9. loc, meanwhile, indexes inclusively. So 0:10 will select entries 0,...,10.
# print(onco.set_index('name'))
Data = pd.DataFrame({'Name':['Riddhi Nashine','shruti','rohan','amruta','jashnavi'],'College':['GHRaisoni','ghraisoni','ghraisoni','ycc','ycc'],'color':['blue','yellow','green','red',None],'marks':[99,83,88,87,86]})
print(Data.loc[Data.color.isnull()])
print(Data)
# print(Data.Name == "shruti")
# print(Data.loc[Data.College == 'ghraisoni'])
# print(Data.loc[(Data.College == 'ghraisoni') | (Data.Name  == 'rohan') ])
# print(Data.loc[(Data.College == 'ghraisoni') & (Data.Name  == 'rohan') ]
# print(Data.loc[Data.color.isin(['red','blue'])])
Data['House'] = 'Same'
Data['index_backward'] = range(len(Data),0,-1)
print(Data)
print(Data.color.describe())
print(Data.marks.mean())
print(Data.color.unique())
print(Data.color.value_counts())

#map
means = Data.marks.mean()
print(Data.marks.map(lambda p : p - means))
def remean_marks(row):
    row.marks = row.marks - means
    return row
Data = Data.apply(remean_marks, axis="columns")
print(Data)
print(Data.head(0))
print(Data.head(1))
print(Data.marks - means)
print(Data.Name + '-' + Data.College)

#grouping and sorting
print(Data.groupby('College').Name.count())
print(Data.groupby('College').marks.mean())
print(Data.groupby('College').marks.min())
print(Data.groupby('College').apply(lambda df : df.Name.iloc[0]))