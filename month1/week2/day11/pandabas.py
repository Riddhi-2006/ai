#GROUPING AND SORTING
import pandas as pd
data = pd.DataFrame({'name':['riddhi','rohan','shruti','amruta','jashnavi','siddhi'],
                     'age':[19,19,20,19,20,19],
                     'surname':['nashine','nandanwar','dhole','gotmare','singdi','gotmare'],
                     'college':['ghraisoni','ghraisoni','ramdeobaba','ycc','ycc','ramdeobaba'],
                     'rollno':[7,37,14,1,3,15],
                     'city':['bhandara','nagpur','nagpur','nagpur','singholi','nagpur']})
print(data)
print(data.groupby('city').age.min())
print(data.groupby('college').apply(lambda df : df['name'].iloc[0]))
print(data.groupby(['city','age']).apply(lambda df : df.loc[df.college.idxmax()]))
print(data.groupby('city').age.agg([max,min,len]))

# multi indexes
print(data.groupby(['college','city']).age.agg([len]))
print(data.index)
#sorting
print(data.reset_index())
print(data.sort_values(by = 'name',ascending = False))
print(data.sort_index())
print(data.sort_values(by = ['city','name','surname']))