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
low_cardinality = [cname for cname in x_train.columns if x_train[cname].nunique() < 10 and x_train[cname].dtype == 'string']
# Select numerical columns
numerical_col = [cname for cname in x_train.columns if x_train[cname].dtype in ['float64','int64'] ]
# Keep selected columns only
my_col = low_cardinality+ numerical_col 

x_trainf = x_train[my_col].copy()
x_valf = x_val[my_col].copy()


# from sklearn.impute import SimpleImputer
# num_imputer = SimpleImputer(strategy='median')
# x_trainf[numerical_col] = num_imputer.fit_transform(x_trainf[numerical_col])
# x_valf[numerical_col] = num_imputer.transform(x_valf[numerical_col])

# cat_imputer = SimpleImputer(strategy='most_frequent')
# x_trainf[low_cardinality] = cat_imputer.fit_transform(x_trainf[low_cardinality])
# x_valf[low_cardinality] = cat_imputer.transform(x_valf[low_cardinality])

print(x_trainf.head())
s = (x_trainf.dtypes == 'str')
print(s)
# boolean indexing s[s] keeps true values only
str_cols = list(s[s].index)
print('categorical variables')
print(str_cols)

from sklearn.metrics import mean_absolute_error
from sklearn.ensemble import RandomForestRegressor
def score_dataset(x_trainf,x_valf,y_train,y_val):
    model = RandomForestRegressor(random_state=8,n_estimators=100)
    model.fit(x_trainf,y_train)
    pred = model.predict(x_valf)
    return mean_absolute_error(y_val,pred)

# APPROACH 1 dropping categorical data
drop_x_train = x_trainf.select_dtypes(exclude = ['str'])
drop_x_val = x_valf.select_dtypes(exclude = ['str'])
print('mae in approach 1 droping categorical variables')
print(score_dataset(drop_x_train,drop_x_val,y_train,y_val))

# APPROACH 2 ordinal encoding
from sklearn.preprocessing import OrdinalEncoder
label_x_train = x_trainf.copy()
label_x_val = x_valf.copy()
ordinal_encoder = OrdinalEncoder()
label_x_train[str_cols] = ordinal_encoder.fit_transform(label_x_train[str_cols])
label_x_val[str_cols] = ordinal_encoder.transform(label_x_val[str_cols])
print('mae in approach 2 orddinal encoder')
print(score_dataset(label_x_train,label_x_val,y_train,y_val))

# APPROACH 3 one hot encoding
from sklearn.preprocessing import OneHotEncoder
onehot_encoder = OneHotEncoder(handle_unknown='ignore',sparse_output=False)
oh_train_col= pd.DataFrame(onehot_encoder.fit_transform(x_trainf[str_cols]))
oh_val_col = pd.DataFrame(onehot_encoder.transform(x_valf[str_cols]))

# One-hot encoding removed index; put it back
oh_train_col.index = x_trainf.index
oh_val_col.index = x_valf.index

# Remove categorical columns (will replace with one-hot encoding)
num_x_train = x_trainf.drop(str_cols,axis =1)
num_x_val = x_valf.drop(str_cols,axis = 1)

# Add one-hot encoded columns to numerical features
oh_x_train = pd.concat([num_x_train,oh_train_col],axis =1)
oh_x_val = pd.concat([num_x_val,oh_val_col],axis =1)

# Ensure all columns have string type
oh_x_train.columns = oh_x_train.columns.astype(str)
oh_x_val.columns = oh_x_val.columns.astype(str)
print('mae approach 3 one hot encoding')
print(score_dataset(oh_x_train,oh_x_val,y_train,y_val))