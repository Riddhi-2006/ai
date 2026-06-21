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
# onco['phone'] = onco['phone'].fillna('unknown')
# print(onco['phone'].isnull().sum())

# onco['website'] = onco['website'].fillna('unknown')
# print(onco['website'].isnull().sum())

# onco['reviewsCount']=onco['reviewsCount'].fillna(onco['reviewsCount'].median())
# print(onco['reviewsCount'].isnull().sum())

#dropping columns having too many missing values
# onco = onco.drop(columns=['reviewsCount'],errors='ignore')
# print(onco.isnull().sum())
# ---- UNIVARIATE ANALYSIS ----
# distribution of reviews count
sns.histplot(onco['reviewsCount'])
plt.title('review count distribution')
# doctors per city
sns.countplot(y='city',data=onco,order=onco['city'].value_counts().index[:10])
plt.title('top 10 cities by doctor couunt')

# ---- BIVARIATE ANALYSIS ----
# top rated doctors
top_rated = onco.sort_values('reviewsCount',ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(x='reviewsCount',y='name',data=top_rated)
plt.title('top 10 doctors by reviews')
# plt.show()
# ---- INSIGHTS ----
print("\n--- KEY INSIGHTS ---")
print(f"Total oncologists: {len(onco)}")
print(f"Cities covered: {onco['city'].nunique()}")
print(f"Average reviews count: {onco['reviewsCount'].mean():.2f}")
print(f"Doctor with most reviews: {onco.loc[onco['reviewsCount'].idxmax(), 'name']}")
print(f"Missing phone numbers: {onco['phone'].isnull().sum()}")
print(f"Missing websites: {onco['website'].isnull().sum()}")
