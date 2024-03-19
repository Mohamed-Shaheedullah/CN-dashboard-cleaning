import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import datetime
from time import gmtime, strftime

df = pd.read_excel("./mb_clean_data/friday_cleaned.xlsx")

total_income_fri = df['Cost'].sum()

print(f"total income is {total_income_fri}")

higest_spend_fri = df["Cost"].max()

print(f"highest_spend is {higest_spend_fri}")

mvp_staff_list_fri = df.groupby('Staff')['Cost'].sum().reset_index()

mvp_top = mvp_staff_list_fri.sort_values(["Cost"], ascending=False, ignore_index=True).head(1)

print(f"MVP for friday is {mvp_top}"   )


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

#### end explode *************************


best_sell_fri = df["Basket"].value_counts().head(1)
print(f"best sell item fri is {best_sell_fri}")

worst_sell_fri = df["Basket"].value_counts().tail(1)
print(f"worst sell item fri is {worst_sell_fri}")


### **********write to file *********
# actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

filename = "./mb_results/friday_results.txt"

outfile = open(filename, "w")
with open(filename, 'a') as outfile:
    outfile.write('\n')
    outfile.write("Total Income : ")
    outfile.write(str(total_income_fri))    
    outfile.write('\n')
    outfile.write("Highest spend : ")
    outfile.write(str(higest_spend_fri))
    outfile.write('\n')
    outfile.write("MVP staff for friday")
    outfile.write(str(mvp_top))
    outfile.write('\n')
    outfile.write("Best selling item : ")
    outfile.write(str(best_sell_fri))
    outfile.write('\n')
    outfile.write("Worst selling item : ")
    outfile.write(str(worst_sell_fri))
    outfile.write('\n')
