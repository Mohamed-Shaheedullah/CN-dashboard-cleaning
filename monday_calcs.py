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

##### explode basket for item info, best and worst selling #####


def remove_punctuation(basket):
    basket = str(basket)
    basket=basket.replace("[", "")
    basket=basket.replace("]", "")
    basket=basket.replace("'", "")
    return basket

df["Basket"] = df["Basket"].apply(remove_punctuation)

def split_basket(basket_str):
    elements = basket_str.split(",")
    return [item.strip() for item in elements]

df["Basket"] = df["Basket"].apply(split_basket)

df = df.explode("Basket", ignore_index=False)


best_sell_mon = df["Basket"].value_counts().head(1)
print(f"best_sell_mon is {best_sell_mon}")

###### WORST SELL MONDAY BELOW ####

