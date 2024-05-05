import os
import pandas as pd



'''IMPORT GOOD AND SERVICES'''
imports = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/importsgoodandservices.csv'

imports_df = pd.read_csv(imports)
imports_df['DATE'] = pd.to_datetime(imports_df['DATE'])
imports_df['Year'] = imports_df['DATE'].dt.year
imports_yearly = imports_df.groupby('Year')['IMPGS'].sum()



'''INTEREST DISCOUNT RATE '''
interest_discount = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/interestdiscount.csv'

interest_df = pd.read_csv(interest_discount)
interest_df['DATE'] = pd.to_datetime(interest_df['DATE'])
interest_df['Year'] = interest_df['DATE'].dt.year

interest_mean = interest_df.groupby('Year')['INTDSRUSM193N'].mean()


'''NEW HOUSE SALES (thousands of units)'''
houses = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/singlefamilyhousessold.xlsx'


houses_df = pd.read_excel(houses, skiprows=7)
houses_df = houses_df[['Period','Value']]
houses_df['New House Sale'] = houses_df['Value']
houses_df['Year'] = pd.to_datetime(houses_df['Period']).dt.year
houses_df = houses_df.dropna(subset=['New House Sale'])
houses_df = houses_df[houses_df['Year'] != 2024]
houses_yearly = houses_df.groupby('Year')['New House Sale'].sum()



'''S&P 500 Returns'''
s_and_p = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/sp-500-historical-annual-returns.csv'

s_and_p_df = pd.read_csv(s_and_p, skiprows=15)
s_and_p_df['Year'] = pd.to_datetime(s_and_p_df['date']).dt.year
s_and_p_df = s_and_p_df.rename(columns={' value': 'S&P Returns'})
s_and_p_df = s_and_p_df[['S&P Returns', 'Year']]



'''UNEMPLOYMENT RATE'''
unemployment = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/unemploymentrate.csv'

unemployment_df = pd.read_csv(unemployment)
unemployment_df['DATE'] = pd.to_datetime(unemployment_df['DATE'])
unemployment_df['Year'] = unemployment_df['DATE'].dt.year

unemployment_mean = unemployment_df.groupby('Year')['UNRATE'].mean()


'''Average M2 (Billions of Dollars)'''

m2 = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/m2.csv'

m2_df = pd.read_csv(m2)
m2_df['Year'] = pd.to_datetime(m2_df['DATE']).dt.year

m2_mean = m2_df.groupby('Year')['WM2NS'].mean()

'''Average GDP (Billions of Chained 2017 Dollars)'''

gdp = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/GDPC1.csv'

gdp_df = pd.read_csv(gdp)
gdp_df['Year'] = pd.to_datetime(gdp_df['DATE']).dt.year


gdp_mean = gdp_df.groupby('Year')['GDPC1'].mean()


'''Treasury Constant'''

treasury = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/T10Y2Y.csv'

treasury_df = pd.read_csv(treasury)
treasury_df['Year'] = pd.to_datetime(treasury_df['DATE']).dt.year


treasury_df['T10Y2Y'] = pd.to_numeric(treasury_df['T10Y2Y'], errors='coerce')
treausry_mean = treasury_df.groupby('Year')['T10Y2Y'].mean()

'''Sticky CPI'''

sticky_cpi = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/sticky_consumer_price_index.csv'

cpi_df = pd.read_csv(sticky_cpi)
cpi_df['Year'] = pd.to_datetime(cpi_df['DATE']).dt.year

cpi_mean = cpi_df.groupby('Year')['CORESTICKM159SFRBATL'].mean()

'''US RMB Exchange Rate'''

china_exchange = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/chinese_exchange.csv'

china_exchange_df = pd.read_csv(china_exchange)
china_exchange_df['Year'] = pd.to_datetime(china_exchange_df['DATE']).dt.year


china_exchange_df['DEXCHUS'] = pd.to_numeric(china_exchange_df['DEXCHUS'],errors='coerce')
china_mean = china_exchange_df.groupby('Year')['DEXCHUS'].mean()


'''US Canadian Exchange Rate'''

canada_exchange = '/Users/joshiebestie/Downloads/linear regression project/time-series-data/canadian_exchange.csv'
canada_df = pd.read_csv(canada_exchange)

canada_df['Year'] = pd.to_datetime(canada_df['DATE']).dt.year

canada_df['DEXCAUS'] = pd.to_numeric(canada_df['DEXCAUS'],errors='coerce')
canada_mean = canada_df.groupby('Year')['DEXCAUS'].mean()




imports_yearly = imports_yearly.to_frame()
interest_mean = interest_mean.to_frame()
houses_yearly = houses_yearly.to_frame()
s_and_p_df = s_and_p_df.set_index('Year')
unemployment_mean = unemployment_mean.to_frame()
m2_mean = m2_mean.to_frame()
gdp_mean = gdp_mean.to_frame()
treausry_mean = treausry_mean.to_frame()
cpi_mean = cpi_mean.to_frame()
china_mean = china_mean.to_frame()
canada_mean = canada_mean.to_frame()

# Concatenate the series and dataframes
combined_df = pd.concat([imports_yearly, interest_mean, houses_yearly, s_and_p_df, unemployment_mean, m2_mean, gdp_mean, treausry_mean,cpi_mean,china_mean,canada_mean], axis=1)

# Drop any rows with NaN values
combined_df = combined_df.dropna()

combined_df = combined_df.reset_index()


print(combined_df)


combined_df.to_csv('time-series-data.csv', index=False)
