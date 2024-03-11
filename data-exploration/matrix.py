
import pandas as pd
import numpy as np
import json

df = pd.read_csv('/Users/joshiebestie/Downloads/linear regression project/trade blocs ntbs.csv')
df_toadd = pd.read_csv('/Users/joshiebestie/Downloads/trade blocs tariffs.csv')

df_combined = pd.concat([df, df_toadd], ignore_index=True)


X = df_combined[['l_lnsmfn', 'dxr', 'imf', 'fsharec', 'wlrcac', 'polity']]
corr_matrix = X.corr()

corr_matrix.to_csv('correlation_matrix.csv')
