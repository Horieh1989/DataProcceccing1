import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

def read_athlete():
    return pd.read_csv('Project/Data/athlete_events.csv')

df = read_athlete()
df.info()
df.describe()
print(f"the number of age value counts: {df['Age'].value_counts(25)}")
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
print(f"name Medal: {df['Medal'].unique()}" )