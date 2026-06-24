import pandas as pd
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error
from sklearn.model_selection import train_test_split 
file_path = "C:/Users/riddh/Downloads/melb_data.csv"
file_data = pd.read_csv(file_path)
file_data = file_data.dropna(axis = 0)
y = file_data.Price
features = ['Rooms', 'Bathroom', 'Landsize', 'Lattitude', 'Longtitude']
X = file_data[features]


train_X,val_X,train_y,val_y = train_test_split(X,y,random_state=1)
model = DecisionTreeRegressor(random_state=1)
model.fit(train_X,train_y)
val_pred = model.predict(val_X)
print(mean_absolute_error(val_y,val_pred))
print(file_data['Price'].mean())

# overfitting underfitting

def get_mae(max_leaf_nodes,train_X,train_y,val_X,val_y):
    model2 = DecisionTreeRegressor(max_leaf_nodes=max_leaf_nodes ,random_state=1)
    model2.fit(train_X,train_y)
    pred = model2.predict(val_X)
    mae = mean_absolute_error(val_y,pred)
    return(mae)

candidate_max_leaf_node = [10,50,100,150,200,250,500,1000,2000,3000,4000,50000]
scores = {}
for max_leaf_nodes in candidate_max_leaf_node :
    my_mae = get_mae(max_leaf_nodes,train_X,train_y,val_X ,val_y)
    scores[max_leaf_nodes] = my_mae
best_fit = min(scores,key = scores.get)
print(scores)
final_model = DecisionTreeRegressor(max_leaf_nodes= best_fit,random_state=42)
final_model.fit(train_X,train_y)
predict = final_model.predict(val_X)
print(mean_absolute_error(val_y,predict))