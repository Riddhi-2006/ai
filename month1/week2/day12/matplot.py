import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Path of the file to read
fifa_filepath = "C:/Users/riddh/Downloads/fifa.csv"
# Read the file into a variable fifa_data
fifa_data = pd.read_csv(fifa_filepath, index_col='Date',parse_dates=True)
# Print the first 5 rows of the data
print(fifa_data.head())
# Set the width and height of the figure
# plt.figure(figsize=(16,6))
# Add title
# plt.title('fifa')
# Line chart showing how FIFA rankings evolved over time
# sns.lineplot(data = fifa_data)
# plt.show()
print(fifa_data.tail())
print(list(fifa_data.columns))
# sns.lineplot(data = fifa_data['BRA'], label='BRA')
# sns.lineplot(data = fifa_data['ESP'], label='ESP')
# plt.show()
# plt.xlabel('y')
# plt.ylabel('x')
# plt.figure(figsize=(16,6))
# sns.barplot(x=fifa_data.index,y=fifa_data['BRA'])
# plt.show()
# plt.figure(figsize=(14,6))
# sns.heatmap(data = fifa_data, annot=False)
# plt.show()
# sns.scatterplot(x=fifa_data['BRA'],y=fifa_data['ESP'])
# plt.show()
# sns.regplot(x=fifa_data['BRA'],y=fifa_data['ESP'])
# sns.scatterplot(x=fifa_data['BRA'],y=fifa_data['ESP'],hue = fifa_data['ARG'])

# sns.lmplot(x='ESP',y='BRA',hue='ITA',data=fifa_data)
# sns.swarmplot(x=fifa_data['BRA'],y=fifa_data['ESP'])

#distributions
# sns.histplot(data=fifa_data['BRA'])
#kernel density estimate (KDE) 
# sns.kdeplot(data=fifa_data['GER'],color='red',shade=True)

# 2D KDE plot
# sns.jointplot(x=fifa_data['BRA'],y=fifa_data['ESP'],kind='kde')
# sns.histplot(data=fifa_data,x='ESP',hue='ITA')
sns.kdeplot(data = fifa_data,x='GER',hue='ARG',shade=True)
# setting style
sns.set_style('dark')
sns.histplot(data=fifa_data)
plt.show()

