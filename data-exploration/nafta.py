import pandas as pd
import os
import numpy as np


os.chdir('/Users/joshiebestie/Downloads/linear regression project/BACI_HS92_V202401/interest folder')

csv_files = [f for f in os.listdir("/Users/joshiebestie/Downloads/linear regression project/BACI_HS92_V202401/interest folder") if f.endswith('.csv')]


dfs = []

for csv in csv_files:
    df = pd.read_csv(os.path.join("/Users/joshiebestie/Downloads/linear regression project/BACI_HS92_V202401/interest folder", csv))
    conditions = (
    ((df['i'] == 842) & df['j'].isin([124, 484])) |  # US importing from Canada or Mexico
    ((df['j'] == 842) & df['i'].isin([124, 484]))    # US exporting to Canada or Mexico
    )

    filtered_df = df.loc[conditions]
    
    dfs.append(filtered_df)


cleaned_dataframes = []
for df in dfs:
    cleaned_df = df.drop(columns=[col for col in df if col.startswith('Unnamed')], errors='ignore')
    cleaned_dataframes.append(cleaned_df)


final_df = pd.concat(cleaned_dataframes, ignore_index=True)
final_df.to_csv('final_usa_data.csv', index=False)

print('hello! this ran')
