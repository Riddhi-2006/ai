import pandas as pd 
from sklearn.model_selection import train_test_split
file_path = "C:/Users/riddh/Downloads/melb_data.csv"
file_data = pd.read_csv (file_path)
y = file_data.Price
x = file_data.drop(['Price'],axis=1)
x_train,x_val,y_train,y_val = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=0)
# Drop columns with missing values (simplest approach)
missing_col = [col for col in x_train.columns if x_train[col].isnull().any()]
x_train.drop(missing_col,axis = 1, inplace = True)
x_val.drop(missing_col,axis = 1, inplace = True)
# "Cardinality" means the number of unique values in a column
# Select categorical columns with relatively low cardinality (convenient but arbitrary)
low_cardinality = [cname for cname in x_train.columns if x_train[cname].nunique() < 10 and x_train[cname].dtype == 'object']
# Select numerical columns
numerical_col = [cname for cname in x_train.columns if x_train[cname].dtype in ['float64','int64'] ]

# Keep selected columns only
my_col = numerical_col + low_cardinality

x_trainf = x_train[my_col].copy()
x_valf = x_val[my_col].copy()
print(x_trainf.head())
