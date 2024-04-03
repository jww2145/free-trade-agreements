import numpy as np 
import pandas as pd


#tariff rates: https://data.worldbank.org/indicator/TM.TAX.MRCH.WM.AR.ZS?locations=US
# mortgate rates: https://fred.stlouisfed.org/series/MORTGAGE30US
# interest: https://tradingeconomics.com/united-states/interest-rate#:~:text=The%20benchmark%20interest%20rate%20in,percent%20in%20December%20of%202008.
# median household income: https://www.statista.com/statistics/200838/median-household-income-in-the-united-states/
# inflation rate: https://tradingeconomics.com/united-states/inflation-cpi#:~:text=Inflation%20Rate%20in%20the%20United%20States%20averaged%203.30%20percent%20from,percent%20in%20June%20of%201921.
# GDP: https://tradingeconomics.com/united-states/gdp#:~:text=GDP%20in%20the%20United%20States,543.30%20USD%20Billion%20in%201960.

#https://tradethatswing.com/average-historical-stock-market-returns-for-sp-500-5-year-up-to-150-year-averages/#:~:text=The%20historical%20average%20yearly%20return,including%20dividends)%20is%206.92%25.
#https://www.statista.com/topics/771/employment/#topicOverview
# https://my.ibisworld.com/us/en/industry-specialized/od4409/at-a-glance

data = np.array([
    ["2014",1.7,4.53, .25,64900,1.5,17.6,11.39,59,.462,7.8],
    ["2015",1.7,3.73,.25,68140,-.1,18.2,-.73,59.3, .432,8.6],
    ["2016",1.6,3.92,.5,70840,1.4,18.7,9.54,59.7,.432,7.2],
    ["2017", 1.7,4.2,.75,72090,2.5,19.5,19.42,60.1,.445,7.7],
    ["2018",1.6,3.95,1.5,73030,2.1,20.5,-6.24,60.4,.445,8.4],
    ["2019",13.8,4.51,2.5,78250,1.6,21.4,28.88,60.8,.54,8.8],
    ["2020",1.5,3.65,1.75,76660,2.5,21.1,16.26,56.8,.54,5.2],
    ["2021",1.5,2.77,.25,76330,1.4,23.3,26.89,58.4,.51,7.7],
    ["2022",3.3,3.11,.25,74580,7.5,25.4,-19.44,60,.51,7.7]
])

df = np.rec.fromarrays(data.T, 
                       names=('Year', 'Tariff_Rates', 'Mortgage_Rates', 'Interest_Rates',
                              'Median_Household_Income', 'Inflation_Rate', 'GDP', 'S&P 500 Returns by Year', 'Employment Rate', 'Percent of Democrats in Congress','Revenue of Strip Clubs in the US (billions)'))

df = pd.DataFrame(df)
