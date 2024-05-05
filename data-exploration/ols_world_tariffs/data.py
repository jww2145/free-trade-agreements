import pandas as pd

df = pd.read_csv('/Users/joshiebestie/Downloads/linear regression project/trade blocs tariffs.csv')
data = df.dropna()
data = data.reset_index(drop=True)
