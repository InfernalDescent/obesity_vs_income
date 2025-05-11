import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.read_csv("income_state_15.csv")
pd.read_csv("obesity_state_15.csv")
obesity_df = pd.read_csv("obesity_state_15.csv")
income_df = pd.read_csv("income_state_15.csv")
income_df = income_df.drop(columns=["Unnamed: 1"])
income_df["Income"] = income_df["Income"].str.replace(",", "")
income_df["Income"] = income_df["Income"].astype(int)
states_merge = pd.merge(income_df,obesity_df, on="State")
plt.figure(figsize=(12, 8))
sns.regplot(x="Income", y="Obesity", data=states_merge, color='salmon')
outliers = ['Louisiana', 'Colorado', 'Alaska', 'Kansas']
overlap = ['Kentucky', 'Arkansas', 'Oklahoma', 'Tennessee', 'West Virginia', 'Oregon', 'New York', 'North Carolina', 'Vermont']
for i, row in states_merge.iterrows():
    if row['State'] in outliers:
        plt.scatter(row['Income'], row['Obesity'], color='crimson', s=30, edgecolor='black', zorder=5)
texts = []
for i, row in states_merge.iterrows():
    if row['State'] not in overlap:
        plt.text(row['Income'], row['Obesity'], row['State'], fontsize=8)
    else:texts.append(plt.text(row['Income'], row['Obesity'], row['State'], fontsize=8))
from adjustText import adjust_text
adjust_text(texts, arrowprops=dict(arrowstyle='->', color='maroon'))
plt.title("Heavy burdens: Exploring the Link Between Low Income and Obesity" )
plt.xlabel("Average Household Income ($)")
plt.ylabel("Obesity Rate (%)")
plt.show()





