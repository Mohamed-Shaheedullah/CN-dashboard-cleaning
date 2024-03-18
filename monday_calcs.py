import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_excel("./mb_clean_data/monday_cleaned.xlsx")

total_income_mon = df['Cost'].sum()

print(f"total income is {total_income_mon}")

higest_spend_mon = df["Cost"].max()

print(f"highest_spend is {higest_spend_mon}")

mvp_staff_mon = df.groupby('Staff')['Cost'].sum().reset_index()

print(mvp_staff_mon.sort_values(["Cost"], ascending=False).head(1))


