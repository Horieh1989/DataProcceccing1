# app.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import hashlib

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Project/Data/athlete_events.csv')
    df.rename(columns={'NOC': 'country'}, inplace=True)
    return df

df = load_data()

st.title("🏅 Olympic Athlete Dashboard")
st.markdown("Explore medal trends, athlete demographics, and sport-specific insights.")

# Sidebar filters
st.sidebar.header("Filters")
selected_country = st.sidebar.selectbox("Select Country", sorted(df['country'].unique()))
selected_sports = st.sidebar.multiselect("Select Sports", sorted(df['Sport'].unique()), default=['Basketball', 'Swimming', 'Speed Skating'])

# Task 1: Medal Distribution
st.header("Task 1: Medal Distribution and Gender Analysis")

medal_counts = df['Medal'].value_counts()
fig1, ax1 = plt.subplots()
medal_counts.plot(kind='bar', color=['gold', 'silver', 'brown'], ax=ax1)
ax1.set_title("Overall Medal Distribution")
st.pyplot(fig1)

gender_counts = df['Sex'].value_counts()
fig2, ax2 = plt.subplots()
gender_counts.plot(kind='bar', color=['blue', 'pink'], ax=ax2)
ax2.set_title("Athlete Gender Distribution")
st.pyplot(fig2)

# Task 2: Sport-Specific Analysis
st.header("Task 2: Sport-Specific Analysis")

sport_df = df[df['Sport'].isin(selected_sports)]

# Medal by country
country_medals = sport_df.groupby(['country', 'Sport'])['Medal'].count().unstack().fillna(0)
fig3, ax3 = plt.subplots()
country_medals.sort_values(by=selected_sports[0], ascending=False).head(10).plot(kind='bar', ax=ax3)
ax3.set_title("Top Countries by Medals in Selected Sports")
st.pyplot(fig3)

# Age distribution
fig4, ax4 = plt.subplots()
sns.boxplot(data=sport_df, x='Sport', y='Age', palette='Set2', ax=ax4)
ax4.set_title("Age Distribution in Selected Sports")
st.pyplot(fig4)

# Gender distribution
gender_sport = sport_df.groupby(['Sport', 'Sex'])['Name'].count().unstack().fillna(0)
fig5, ax5 = plt.subplots()
gender_sport.plot(kind='bar', stacked=True, color=['blue', 'pink'], ax=ax5)
ax5.set_title("Gender Distribution in Selected Sports")
st.pyplot(fig5)

# Task 3: Norway Focus
st.header("Task 3: Norway Medal Insights")

norway_df = df[df['country'] == 'NOR']
medals_by_year = norway_df.groupby("Year")["Medal"].count()
fig6, ax6 = plt.subplots()
medals_by_year.plot(kind="bar", color="darkred", ax=ax6)
ax6.set_title("Norway Medals per Olympic Games")
st.pyplot(fig6)

# Medal type pie chart
medals = norway_df['Medal'].value_counts()
fig7, ax7 = plt.subplots()
colors = ["gold", "silver", "peru"]
ax7.pie(medals, labels=medals.index, autopct="%1.1f%%", colors=colors, startangle=140)
ax7.set_title("Norway's Olympic Medals by Type")
st.pyplot(fig7)
