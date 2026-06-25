import pandas as pd
from sklearn.model_selection import train_test_split

file_path = "C:/Users/riddh/Downloads/melb_data.csv"
data = pd.read_csv(file_path)

y = data.Price
# To keep things simple, we'll use only numerical predictors
data_pred = data.drop(['Price'],axis = 1)
x = data_pred.select_dtypes(exclude=['object'])

x_train,x_val,y_train,y_val = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=7)

#Define Function to Measure Quality of Each Approach

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
def score_dataset(x_train,x_val,y_train,y_val):
    model = RandomForestRegressor(random_state=7)
    model.fit(x_train,y_train)
    pred = model.predict(x_val)
    return mean_absolute_error(y_val,pred)

#Score from Approach 1 (Drop Columns with Missing Values)
# Get names of columns with missing values
missing_cols = [col for col in x_train.columns
                if x_train[col].isnull().any()]
reduced_train_x = x_train.drop(missing_cols,axis = 1)
reduced_val_x = x_val.drop(missing_cols,axis = 1)
print('approach 1 (dropping columns with missing values)')
print(score_dataset(reduced_train_x,reduced_val_x,y_train,y_val))

#Score from Approach 2 (Imputation) (to replace missing values with the mean value along each column)
from sklearn.impute import SimpleImputer
my_imputer = SimpleImputer()
imputed_x_train = pd.DataFrame(my_imputer.fit_transform(x_train))
imputed_x_val = pd.DataFrame(my_imputer.transform(x_val))
#gives back column name which was stripped away during transformation as it imputer concerts it to array
imputed_x_train.columns = x_train.columns
imputed_x_val.columns = x_val.columns
print('approach2 imputation')
print(score_dataset(imputed_x_train,imputed_x_val,y_train,y_val))

#Score from Approach 3 (An Extension to Imputation) keeping track which were nan creating new columns
# Make copy to avoid changing original data (when imputing)
x_train_plus = x_train.copy()
x_val_plus = x_val.copy()

for col in missing_cols:
    x_train_plus[col + 'is missing'] = x_train_plus[col].isnull()
    x_val_plus[col + 'is missing'] = x_val_plus[col].isnull()
imputed_x_train_plus = pd.DataFrame(my_imputer.fit_transform(x_train_plus))
imputed_x_vall_plus = pd.DataFrame(my_imputer.transform(x_val_plus))
imputed_x_train_plus.columns = x_train_plus.columns
imputed_x_vall_plus.columns = x_val_plus.columns
print('approach 3 ')
print(score_dataset(imputed_x_train_plus,imputed_x_vall_plus,y_train,y_val))

print(data.Price.mean())

# Shape of training data (num_rows, num_columns)
print(x_train.shape)
# Number of missing values in each column of training dat
missing_val_count_by_column = x_train.isnull().sum()
print(missing_val_count_by_column)
print(missing_val_count_by_column[missing_val_count_by_column > 0])
 