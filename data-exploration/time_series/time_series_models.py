import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import statsmodels.stats.api as sms
from glmnet import ElasticNet as EN
from sklearn.linear_model import ElasticNet



df = pd.read_csv('/Users/joshiebestie/Coding Projects/free-trade-agreements/data-exploration/merged_data.csv')
data = df.dropna()

y = data['Quantity in Million Metric Tons_Import']
X = data[['Interest_Rates', 'Percent of Democrats in Congress', 'S&P 500 Returns by Year', 'GDP', 'Employment Rate']]
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
