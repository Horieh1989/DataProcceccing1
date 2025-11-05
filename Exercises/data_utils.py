import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np



def read_student():
    return pd.read_csv ('stocksdata\student-mat-missing-data (1).csv')

df=read_student()

print(type(df))
print(f"This is head: {df.head()}")
df.info()
print(f"This is describe: {df.describe()}")
print(df["age"].value_counts())



def plot_missing_values(df):
  missing=df.isnull().sum()
  missing=missing[missing>0].sort_values(ascending=False)
  if missing.empty:
    print("No missin value found in data")
  return

  plt.figure(figsize=(2,6))
  sns.barplot(x=missing.values,y=missing.index,palette="viridis") 
  plt.title("Missing Values per Column")
  plt.xlabel("Number of Missing Values")
  plt.ylabel("Columns")
  plt.tight_layout()
  plt.show()


    
 