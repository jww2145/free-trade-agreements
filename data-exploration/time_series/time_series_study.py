import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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

# Create a figure and axes
fig, ax = plt.subplots(figsize=(10, 6))

# Create a table using the summary DataFrame
table = ax.table(cellText=summary.values, colLabels=summary.columns, rowLabels=summary.index, loc='center')

# Adjust the table properties
table.auto_set_font_size(False)
table.set_fontsize(12)
table.scale(1.2, 1.2)
table.auto_set_column_width(col=list(range(len(summary.columns))))


# Remove the axes
ax.axis('off')

# Add a title
ax.set_title('Statistical Summary')

# Adjust the layout and display the plot
fig.tight_layout()
plt.show()