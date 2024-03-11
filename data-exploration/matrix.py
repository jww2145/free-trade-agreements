
import pandas as pd
import numpy as np
import json
from scipy.stats import chi2_contingency

df = pd.read_csv('/Users/joshiebestie/Downloads/linear regression project/trade blocs ntbs.csv')


X = df[['l_lnntb', 'lngdppc', 'wlxm', 'wlrca', 'ntbcov']]
corr_matrix = X.corr()

print(corr_matrix)
