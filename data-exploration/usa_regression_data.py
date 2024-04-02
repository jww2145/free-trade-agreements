import numpy as np
import pandas as pd
from usa_indepedent_variables import df

data = pd.read_csv('/Users/joshiebestie/Coding Projects/free-trade-agreements/data-exploration/final_usa_data.csv')

data['q'] = data['q'].replace('NA', np.nan)
data = data.dropna(subset=['q'])
data['q'] = pd.to_numeric(data['q'], errors='coerce')

data['trade_type'] = np.where(data['i'] == 842, 'Export', 'Import')

result = data.groupby(['t', 'trade_type']).agg({'v': 'sum', 'q': 'sum'}).reset_index()

result['v'] = result['v']/1e6
result['q'] = result['q']/1e6

result = result.rename(columns={'v': 'Value in Billions USD', 'q': 'Quantity in Million Metric Tons'})

result_pivot = result.pivot(index='t', columns='trade_type', values=['Value in Billions USD', 'Quantity in Million Metric Tons'])
result_pivot.columns = ['_'.join(col) for col in result_pivot.columns]
result_pivot = result_pivot.reset_index()

result_pivot = result_pivot.rename(columns={'t': 'Year'})

result_pivot['Year'] = result_pivot['Year'].astype(int)
df['Year'] = df['Year'].astype(int)


merged_df = pd.merge(result_pivot, df, on='Year', how='inner')
file_path = '/Users/joshiebestie/Coding Projects/free-trade-agreements/data-exploration/merged_data.csv'
merged_df.to_csv(file_path,index=True)

print(merged_df)