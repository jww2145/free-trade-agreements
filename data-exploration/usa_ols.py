import pandas as pd
import statsmodels.api as sm
import plotly.graph_objects as go




df = pd.read_csv('/Users/joshiebestie/Coding Projects/free-trade-agreements/data-exploration/merged_data.csv')

data = df.dropna()
Y = data['Value in Billions USD_Export']
X = data[['Tariff_Rates', 'Mortgage_Rates', 'Interest_Rates', 'Median_Household_Income', 'Inflation_Rate', 'GDP']]

X = sm.add_constant(X)

model = sm.OLS(Y, sm.add_constant(X)).fit()

print(model.summary())
