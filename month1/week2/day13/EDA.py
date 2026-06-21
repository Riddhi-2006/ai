#EDA (Exploratory Data Analysis)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
file_path = "C:/Users/riddh/Downloads/oncologists_nyc.csv"
onco = pd.read_csv(file_path)
print(onco.head())
print(onco.tail())
print(onco.name)
print(onco.shape)
print(onco.describe())
print(onco.info())
print(onco.columns)
# checking missing values
print(onco.isnull().sum())
# visualizing missing values
# sns.heatmap(onco.isnull())
# plt.title('missing value heatmap')
# plt.show()
# handle missing data
onco['phone'] = onco['phone'].fillna('unknown')
print(onco['phone'].isnull().sum())

onco['website'] = onco['website'].fillna('unknown')
print(onco['website'].isnull().sum())

onco['reviewsCount']=onco['reviewsCount'].fillna(onco['reviewsCount'].median())
print(onco['reviewsCount'].isnull().sum())

#dropping columns having too many missing values
onco = onco.drop(columns=['reviewsCount'],errors='ignore')
print(onco.isnull().sum())
print