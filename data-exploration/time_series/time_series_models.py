import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import statsmodels.stats.api as sms
from glmnet import ElasticNet as EN
from sklearn.linear_model import ElasticNet
from sklearn.preprocessing import MinMaxScaler


df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')
data = df.dropna()

# Assuming your dataframe is named 'df'
columns_to_normalize = ['IMPGS', 'INTDSRUSM193N', 'New House Sale', 'S&P Returns', 'UNRATE', 'WM2NS', 'GDPC1', 'T10Y2Y', 'CORESTICKM159SFRBATL', 'DEXCHUS', 'DEXCAUS']

scaler = MinMaxScaler()
data[columns_to_normalize] = scaler.fit_transform(df[columns_to_normalize])

y = data['IMPGS']
X = data[['New House Sale', 'T10Y2Y', 'S&P Returns', 'DEXCHUS', 'UNRATE', 'DEXCAUS']]
X = sm.add_constant(X)


'''
OLS Model
'''

ols_model = sm.OLS(y, X)
 
# Conduct the Breusch-Pagan test
names = ['Lagrange multiplier statistic', 'p-value',
         'f-value', 'f p-value']
 
# Get the test result
test_result = sms.het_breuschpagan(ols_model.fit().resid, ols_model.fit().model.exog)

print(ols_model.fit().summary())
'''
WLS Model

Maybe perform test for heteroskedasticity
'''

residuals = ols_model.fit().resid
fitted_values = (ols_model.fit().fittedvalues)
fitted_values = sm.add_constant(fitted_values)


test = sm.OLS(abs(residuals),fitted_values).fit()


weights = (1 / (test.fittedvalues))**2



#I use the inverse of the standard error as my weights


wls_model = sm.WLS(y,X,weights).fit()

std_err_resid = np.sqrt(wls_model.scale)


print(wls_model.summary())
'''
GLS Model

Test for normality
'''

sigma = np.cov(residuals)

gls_model = sm.GLS(y,X,sigma).fit()

print(gls_model.summary())


'''
Lasso
'''

cv_model = EN(alpha = 1)
cv_model.fit(X,y)

print(cv_model.lambda_best_)



model = ElasticNet(l1_ratio = 1, alpha = 112.1942)
model.fit(X, y)
coefficients = pd.DataFrame(model.coef_, index=X.columns, columns=['Coefficient'])

print(coefficients)
