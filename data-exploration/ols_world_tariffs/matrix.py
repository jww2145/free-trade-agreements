
import pandas as pd


df = pd.read_csv('/Users/joshiebestie/Downloads/trade blocs tariffs.csv')

data = df.dropna()


X = data[['l_lnsmfn', 'dxr', 'imf', 'fsharec', 'wlrcac', 'polity']]
corr_matrix = X.corr()
corr_matrix.to_csv('correlation_matrix.csv')
