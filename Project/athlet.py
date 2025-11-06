import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

#0
def read_athlete():
    return pd.read_csv('Project/Data/athlete_events.csv')

df = read_athlete()
df.info()
df.describe()
print(f"the number of age value counts: {df['Age'].value_counts()}")
row,col = df.shape
print(f"Number of rows: {row}, Number of columns: {col}")
print(f" the number of countries: {df['NOC'].nunique()}")
print(df.columns)
print(df.head(15))
df.rename(columns={'NOC':'country'}, inplace=True)
print(f"name of columns: {df.columns}")
print(f"name countries: {df['country'].nunique()}" )
print(f"name Games: {df['Games'].unique()}" )
print(f"name Sport: {df['Sport'].unique()}" )
print(f"type of  Medal: {df['Medal'].unique()}" )
print(f"list of Age : {df['Age'].unique()}" )
print(f"the number of age unique: {df['Age'].value_counts()}")
minimum=df['Age'].min()
maximum=df['Age'].max()
mean_age=df['Age'].mean()
median_age=df['Age'].median()

print(f"Minimum age: {minimum}, Maximum age: {maximum}, Mean age: {mean_age}, Median age: {median_age}")


df['Sex'].value_counts().plot(kind='bar', color=['blue', 'pink'])
plt.title('Distribution of Athletes by sex')
plt.xlabel('Sex')
plt.ylabel('Number of Athletes')
plt.show()
df['Medal'].value_counts().plot(kind='bar', color=['gold', 'silver', 'brown'])
plt.title('Distribution of Medals')
plt.xlabel('Medal')
plt.ylabel('Number of Medals')
plt.show()

Most_Medals_Country=df.groupby('country')['Medal'].count().sort_values(ascending=False).head(10)
print("Top 10 countries with most medals:")
print(Most_Medals_Country)



plt.figure(figsize=(10,6))
sns.histplot(x=Most_Medals_Country.index, y=Most_Medals_Country.values, bins=10, kde=False, color='blue' )
plt.title('Top 10 Countries with Most Medals')
plt.xlabel('Country')
plt.ylabel('Number of Medals')
plt.xticks(rotation=45)
plt.show()
