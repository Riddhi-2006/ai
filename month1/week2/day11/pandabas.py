#GROUPING AND SORTING
import pandas as pd
data = pd.DataFrame({'name':['riddhi','rohan','shruti','amruta','jashnavi','siddhi'],
                     'age':[19,19,20,19,20,19],
                     'surname':['nashine','nandanwar','dhole',None,'singdi','gotmare'],
                     'college':['ghraisoni',None,'ramdeobaba','ycc','ycc','ramdeobaba'],
                     'rollno':[7,37,14,1,3,15],
                     'city':['bhandara','nagpur',None,'nagpur','singholi','nagpur']})
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
# datatypes
print(data.age.dtype)
print(data.dtypes)
print(data.age.astype('float16'))
print(data.index.dtype)
#missing data
print(data[pd.isnull(data.city)])
print(data.city.fillna('unknown'))
print(data.name.replace('riddhi','Riddhi'))
data['name'] = data.name.replace('riddhi','Riddhi')
print(data)
# rename and combining
print(data.rename(columns={'name':'first name'}))
data = data.rename(columns={'name':'fname'})
print(data)
print(data.rename(index={ 0 :'first'}))
print(data.rename_axis('index',axis = 'rows').rename_axis('field', axis = 'columns'))
print(data.to_markdown(index=True, tablefmt="grid"))
data2 = pd.DataFrame({'nam':['riddhi','kan'],
                     'cit':['nhg','khj']})
print(pd.concat([data,data2]))
left = data.set_index(['city'])
right = data2.set_index(['cit'])
print(left.join(right, lsuffix='l',rsuffix='r'))