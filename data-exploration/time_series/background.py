import pandas as pd 

df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')

print("Import goods and services between 1994 and 1999  :", df[['IMPGS']].where((1994 <= df['Year']) & (df['Year']<1999)).dropna().sum())

print("Import goods and services between 1989 and 1994  :", df[['IMPGS']].where((1989 <= df['Year']) & (df['Year']<1994)).dropna().sum())