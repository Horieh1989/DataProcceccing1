import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import hashlib 


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

#The top 10 countries with the most medals
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

Number_of_medals=df[df['country'] == 'NOR']['Medal'].count()
Medal_distribution=df[df['country'] == 'NOR']['Medal'].value_counts()
Medal_distribution.plot(kind='bar', color=['gold', 'silver', 'brown'])
    
plt.title(f'Medal Distribution for NORway: Total Medals = {Number_of_medals}')
plt.xlabel('Medal')     
plt.ylabel('Number of Medals')
plt.show()

#1

# Save Norway athlete data to a new CSV file/4960row and 15columns
Norway_data=df[df['country'] == 'NOR']
Norway_data.to_csv('Project/Data/Norway_athlete_data.csv', index=False)

dfN=pd.read_csv('Project/Data/Norway_athlete_data.csv')
def hash_name(name):
    return hashlib.sha256(name.encode()).hexdigest()

#apply hash function to Name column and save to a csv file
dfN["Name"] = dfN["Name"].apply(hash_name)
dfN.to_csv("Project/Data/Norway_athlete_data_anonymized.csv", index=False)

#Sports where the country has won the most medals
Most_Medals_Sport=dfN.groupby('Sport')['Medal'].count().sort_values(ascending=False).head(10)
print(f"Top 10 Sports with most medals for NORway: {Most_Medals_Sport}")

#plot for sports with most medals 
import matplotlib.pyplot as plt

Most_Medals_Sport.head(10).plot(kind="barh", color="steelblue")
plt.title("Top 10 Sports by Medal Count Norway")
plt.xlabel("Number of Medals")
plt.ylabel("Sport")
plt.tight_layout()
plt.show()

#Number of medals per Olympic Games 
medals_by_year = dfN.groupby("Year")["Medal"].count()
print(f"Medals by Year for NORway: {medals_by_year}")
medals_by_year.plot(kind="bar", color="darkred")
plt.title("Norway  Medals per Olympic Games")
plt.xlabel("Olympic Year")
plt.ylabel("Number of Medals")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#2 Analyze age distribution of Norwegian athletes
# Are most medalists in their 20s?
# Is there a wide age range in certain sports?
# Do younger or older athletes dominate?

Norway_data["Age"].plot(kind="hist", bins=10, color="skyblue", edgecolor="black")
plt.title("Age Distribution of Norwegian Olympic Athletes")
plt.xlabel("Age")
plt.ylabel("Number of Athletes")
plt.tight_layout()
plt.show()

# questions:
#1.how many percents took Gold, Silver and Bronze

Medals=dfN['Medal'].value_counts()
colors = ["gold", "silver", "peru"]  # bronze-like color
plt.figure(figsize=(6,6))
plt.pie(Medals, labels=Medals.index, autopct="%1.1f%%", colors=colors, startangle=140)
plt.title("Norway's Olympic Medals by Type")
plt.axis("equal")
plt.show()

# Question 2:
# Medals won by gender
gender_medals = dfN.groupby(["Sex", "Medal"]).size().unstack(fill_value=0)
print(gender_medals)
import matplotlib.pyplot as plt

gender_medals.plot(kind="bar", figsize=(8,6), color=["gold", "silver", "peru"])
plt.title("Norway Olympic Medals by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Medals")
plt.xticks(rotation=0)
plt.legend(title="Medal Type")
plt.tight_layout()
plt.show()


# Question 3:
# Group by Season and Medal type
season_medals = dfN.groupby(["Season", "Medal"]).size().unstack(fill_value=0)
print(season_medals)

season_medals.plot(kind="bar", figsize=(8,6), color=["gold", "silver", "peru"])
plt.title("Norway's Olympic Medals: Summer vs Winter Games")
plt.xlabel("Olympic Season")
plt.ylabel("Number of Medals")
plt.xticks(rotation=0)
plt.legend(title="Medal Type")
plt.tight_layout()
plt.show()



#2

