
import pandas as pd


df = pd.read_csv('/Users/joshiebestie/Coding Projects/free-trade-agreements/data-exploration/merged_data.csv')

data = df.dropna()


X = data[['Value in Billions USD_Export', 'Value in Billions USD_Import', 'Quantity in Million Metric Tons_Export', 'Quantity in Million Metric Tons_Import', 'Tariff_Rates', 'Mortgage_Rates', 'Interest_Rates', 'Median_Household_Income', 'Inflation_Rate', 'GDP']]
corr_matrix = X.corr()
print(corr_matrix)
