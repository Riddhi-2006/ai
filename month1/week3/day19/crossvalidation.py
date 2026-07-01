import pandas as pd
file_path = "C:/Users/riddh/Downloads/melb_data.csv"
data = pd.read_csv(file_path)
cols_to_use = ['Rooms', 'Distance', 'Landsize', 'BuildingArea', 'YearBuilt']
x = data[cols_to_use]
y = data.Price

from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor
from sklearn.impute import SimpleImputer

my_pipeline = Pipeline(steps=[('preprocessor',SimpleImputer()),
                              ('model',RandomForestRegressor(n_estimators=100,random_state=43))])
from  sklearn.model_selection import cross_val_score
scores = -1 * cross_val_score(my_pipeline,x,y,cv=5,scoring='neg_mean_absolute_error')
print('mae scores',scores)
print(scores.mean())
print(data['Price'].mean())