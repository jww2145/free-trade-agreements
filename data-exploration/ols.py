import pandas as pd
import statsmodels.api as sm


df = pd.read_csv('/Users/joshiebestie/Downloads/trade blocs tariffs.csv')

data = df.dropna()
cluster_var = data['isocode']
Y = data['dlnsmfn']
X = data[['l_lnsmfn', 'dxr', 'imf', 'fsharec', 'wlrcac', 'polity']]

X = sm.add_constant(X)

model = sm.OLS(Y, sm.add_constant(X)).fit('pinv','cluster',{'groups': cluster_var})

print(model.summary())

model_summary = model.summary().as_csv()
with open('model_summary.csv', 'w') as file:
    file.write(model_summary)