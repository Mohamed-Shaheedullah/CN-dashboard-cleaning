import pandas as pd
import openpyxl
import numpy as np
import matplotlib.pyplot as plt
import datetime
from time import gmtime, strftime

df = pd.read_excel("./mb_clean_data/thursday_cleaned.xlsx")

total_income_thur = df['Cost'].sum()

print(f"total income is {total_income_thur}")

higest_spend_thur = df["Cost"].max()

print(f"highest_spend is {higest_spend_thur}")

mvp_staff_list_thur = df.groupby('Staff')['Cost'].sum().reset_index()

mvp_top = mvp_staff_list_thur.sort_values(["Cost"], ascending=False, ignore_index=True).head(1)

print(f"MVP for thursday is {mvp_top}"   )

##### for bar chart ################
payment_methods = df.groupby("Payment Method")["Transaction ID"].count().reset_index()

print(payment_methods.info())


payment_types = payment_methods["Payment Method"].to_list()

ax = payment_methods[["Transaction ID"]].plot(kind='bar', title ="Payment Methods", figsize=(10, 6), legend=True, fontsize=12)
ax.set_xlabel("Payment Method", fontsize=12)
ax.set_ylabel("Number of Transactions", fontsize=12)
plt.xticks(range(len(payment_types)), payment_types)
plt.show()
# print("Payment Methods")
# print(payment_methods)
############### end bar chart ################


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


best_sell_thur = df["Basket"].value_counts().head(1)
print(f"best sell item thur is {best_sell_thur}")

worst_sell_thur = df["Basket"].value_counts().tail(1)
print(f"worst sell item thur is {worst_sell_thur}")

###########  copy to other files

all_sold_items = df["Basket"].value_counts() 

print("All sold items Thursday")
print(all_sold_items)
########## end copy ##########################



### **********write to file *********
# actual_time = strftime("%Y-%m-%d %H-%M-%S", gmtime())

filename = "./mb_results/thursday_results.txt"

# outfile = open(filename, "w")
# with open(filename, 'a') as outfile:
#     outfile.write('\n')
#     outfile.write("Total Income : ")
#     outfile.write(str(total_income_thur))    
#     outfile.write('\n')
#     outfile.write("Highest spend : ")
#     outfile.write(str(higest_spend_thur))
#     outfile.write('\n')
#     outfile.write("MVP staff for thursday")
#     outfile.write(str(mvp_top))
#     outfile.write('\n')
#     outfile.write("Best selling item : ")
#     outfile.write(str(best_sell_thur))
#     outfile.write('\n')
#     outfile.write("Worst selling item : ")
#     outfile.write(str(worst_sell_thur))
#     outfile.write('\n')


# Plotting the bar chart
max_item = all_sold_items.idxmax()
plt.figure(figsize=(10, 6))
all_sold_items.plot(kind='bar')
colors = ['purple' if item == max_item else '#1f77b4' for item in all_sold_items.index]
plt.bar(all_sold_items.index, all_sold_items.values, color=colors)
plt.xlabel('Item')
plt.ylabel('Frequency')
plt.title('Frequency of Sold Items on Thursday')
plt.xticks(rotation=45)
plt.tight_layout() 
plt.show()

# pie_chart
color_dict = {
    'Cash': '#1f77b4',
    'Credit': 'purple',
    'Debit': 'blue',
    'Voucher': 'lightblue'
}
labels = payment_methods["Payment Method"]
sizes = payment_methods["Transaction ID"]
colors = [color_dict[label] for label in labels] 
plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', textprops={'color': 'white'})
for autotext in autotexts:
    autotext.set_fontsize(8)
for text in texts:
    text.set_color('black')
    text.set_fontsize(10)  
plt.title('Payment_Methods on Thursday')
# plt.savefig('payment pie friday.png')
plt.show()