import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_excel(r"./mb_dash_week/wednesday_data.xlsx")

## check for duplicates
duplicate_values = df1.duplicated()
print(f"duplicates {duplicate_values.value_counts()}")

# print(df1.head())

# print(df1.info())

# print(df1.describe())

df1 = df1.dropna(how="any")

df1 = df1.drop(columns=["Till ID"])

# print(df1.head())

# print(df1.info())

# print(df1.describe())

b_plot = df1.boxplot(column = 'Cost') 
plt.title("Boxplot for Cost")
plt.show()

b_plot_2 = df1.boxplot(column = 'Total Items') 
plt.title("Boxplot for Total Items")
plt.show()

b_plot_3 = df1.boxplot(column = 'Transaction ID') 
plt.title("Boxplot for Transaction ID")
plt.show()

df1.to_excel("./mb_clean_data/wednesday_cleaned.xlsx")
