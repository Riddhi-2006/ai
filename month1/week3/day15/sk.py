import pandas as pd


file_path="C:/Users/riddh/Downloads/melb_data.csv"
file_data = pd.read_csv(file_path)
print(file_data.columns)
# The Melbourne data has some missing values (some houses for which some variables weren't recorded.)
# We'll learn to handle missing values in a later tutorial.  
# Your Iowa data doesn't have missing values in the columns you use. 
# So we will take the simplest option for now, and drop houses from our data. 
# Don't worry about this much for now, though the code is:

# dropna drops missing values (think of na as "not available")
file_data = file_data.dropna(axis = 0)
# print(file_data.isnull().sum())
#Selecting The Prediction Target
y = file_data.Price
#Choosing "Features"
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = file_data[features]
print(X.describe())
print(X.head())
# The steps to building and using a model are:

# Define: What type of model will it be? A decision tree? Some other type of model? Some other parameters of the model type are specified too.
# Fit: Capture patterns from provided data. This is the heart of modeling.
# Predict: Just what it sounds like
# Evaluate: Determine how accurate the model's predictions are.

from sklearn.tree import DecisionTreeRegressor
# # Define model. Specify a number for random_state to ensure same results each run
# data_model = DecisionTreeRegressor(random_state=1)
# # Fit model
# data_model.fit(X,y)
# print('making predictions for the following five houses')
# print(X.head())
# print('the predictions are')
# print(data_model.predict(X.head()))

# # MODEL VALIDATION

from sklearn.metrics import mean_absolute_error
# predicted_home_prices = data_model.predict(X)
# print(mean_absolute_error(y,predicted_home_prices))

# TRAIN TEST SPLIT OF DATA

from sklearn.model_selection import train_test_split
# split data into training and validation data, for both features and target
# The split is based on a random number generator. Supplying a numeric value to
# the random_state argument guarantees we get the same split every time we
# run this script.
train_X ,val_X,train_y,val_y = train_test_split(X,y,random_state=0)
# Define model
data_model = DecisionTreeRegressor()
# Fit model
data_model.fit(train_X,train_y)
# get predicted prices on validation data
val_prediction = data_model.predict(val_X)
print(mean_absolute_error(val_y,val_prediction))
print(file_data['Price'].mean())
