import pandas as pd
import matplotlib.pyplot as plt
import csv

df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')

'''
plt.figure(figsize=(10, 6))  # Adjust the figure size as needed

plt.plot(df['Year'],df['IMPGS'])
plt.ylabel("Import Good and Services (Billions USD)")
plt.xlabel("Year")


plt.axvline(x = 1994, color = 'red', linestyle = "--", linewidth = 1.5, label = "NAFTA")
plt.text(1994, plt.ylim()[1] * 0.95, 'NAFTA Established', color='red', ha='right', va='top', rotation=90)
plt.show()
'''

# Assuming you have a DataFrame called 'df'
summary = df.describe().round(2)
summary = summary.drop(columns=['Year'])
summary = summary.drop(index = ['count'])

with open('summary_data.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([''] + summary.columns.tolist())  # Write column headers
    for index, row in summary.iterrows():
        writer.writerow([index] + row.tolist())  # Write row labels and data