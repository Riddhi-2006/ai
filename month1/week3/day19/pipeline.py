import pandas as pd
from sklearn.model_selection import train_test_split
file_path = "C:/Users/riddh/Downloads/melb_data.csv"
data = pd.read_csv(file_path)
y = data.Price
x = data.drop(['Price'],axis = 1)
x_train_full,x_val_full,y_train,y_val = train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=43)
categorical_col = [col for col in x_train_full.columns if x_train_full[col].nunique() < 10 and x_train_full[col].dtype == 'str']
numerical_col = [col for col in x_train_full.columns if x_train_full[col].dtype in ['int64','float64']]
my_cols = categorical_col + numerical_col
x_train = x_train_full[my_cols].copy()
x_val = x_val_full[my_cols].copy()
print(x_train.head())
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

# Preprocessing for numerical data
numerical_transfromer = SimpleImputer(strategy='mean')
categorical_transformer = Pipeline(steps=[
    ('imputer',SimpleImputer(strategy='most_frequent')),
    ('onehot',OneHotEncoder(handle_unknown='ignore'))
])
# Bundle preprocessing for numerical and categorical data
preprocessor = ColumnTransformer(transformers=[
    ('nums',numerical_transfromer,numerical_col),
    ('cat',categorical_transformer,categorical_col)
])

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(n_estimators=1000,random_state=43)

from sklearn.metrics import mean_absolute_error
# Bundle preprocessing and modeling code in a pipeline
my_pipeline = Pipeline(steps=[('preprocessor',preprocessor),
                              ('model',model)])
# Preprocessing of training data, fit model
my_pipeline.fit(x_train,y_train)
# Preprocessing of validation data, get predictions
pred = my_pipeline.predict(x_val)
print(mean_absolute_error(y_val,pred))
