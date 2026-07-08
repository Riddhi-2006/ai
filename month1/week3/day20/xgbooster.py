import pandas as pd
from sklearn.model_selection import train_test_split
data = pd.read_csv("C:/Users/riddh/Downloads/melb_data.csv")
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
x = data[cols_to_use]
y = data.Price
x_train,x_val,y_train,y_val=train_test_split(x,y,train_size=0.8,test_size=0.2,random_state=2)

from xgboost import XGBRegressor
model = XGBRegressor( n_estimators= 500,early_stopping_rounds =5,learning_rate=0.05,n_jobs=4)
model.fit(x_train,y_train,eval_set = [(x_val,y_val)],verbose = False)
from sklearn.metrics import mean_absolute_error
pred = model.predict(x_val)
print(mean_absolute_error(y_val,pred))