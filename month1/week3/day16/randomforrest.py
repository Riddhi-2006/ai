import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split
file_path = "C:/Users/riddh/Downloads/melb_data.csv"
file_data = pd.read_csv(file_path)
file_data = file_data.dropna(axis = 0)

y = file_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = file_data[features]
train_X,val_X,train_y,val_y = train_test_split(X,y,random_state=1)
forest_model = RandomForestRegressor(random_state=1)
forest_model.fit(train_X,train_y)
pred = forest_model.predict(val_X)
print(mean_absolute_error(val_y,pred))
print(file_data['Price'].mean())