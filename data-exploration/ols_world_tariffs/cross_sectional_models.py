from data import data
import pandas as pd
import numpy as np
import statsmodels.api as sm
from sklearn.preprocessing import StandardScaler
import statsmodels.formula.api as smf
from statsmodels.compat import lzip
import statsmodels.stats.api as sms



X = data[['l_lnsmfn', 'dxr', 'imf', 'fsharec', 'wlrcac', 'polity']]
X = sm.add_constant(X)
y = data['dlnsmfn']


'''
Below is our OLS model
'''

ols_model = sm.OLS(y, X)
print(ols_model.fit().summary())

# Conduct the Breusch-Pagan test
names = ['Lagrange multiplier statistic', 'p-value',
         'f-value', 'f p-value']
 
# Get the test result
test_result = sms.het_breuschpagan(ols_model.fit().resid, ols_model.fit().model.exog)

print(lzip(names, test_result))

'''
Now, we start the WLS
'''
    
residuals = ols_model.fit().resid
error_variance = np.var(residuals)

#I use the inverse of the standard error as my weights
wi = 1 / error_variance
wi = pd.Series(wi, index=X.index)

wls_model = sm.WLS(y,X,wi).fit()

print(wls_model.summary())


'''
Now the GLS
'''

sigma = np.cov(residuals)

gls_model = sm.GLS(y,X,sigma).fit()

print(gls_model.summary())

'''
Lasso Regression
'''

start = np.array([1.1532,-.4776,.2784,.0604,-.0005,.1584,-.0345])

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X.iloc[:, 1:])  # Assuming the first column is the intercept
X_standardized = np.hstack((np.ones((X_scaled.shape[0], 1)), X_scaled))  # Add back the intercept

# Fit Lasso (Elastic Net with alpha = 1)
lasso = sm.OLS(y, X_standardized).fit_regularized(method='elastic_net',
                                                  alpha=0.04051121,
                                                  L1_wt=1.0,
                                                  start_params=start,
                                                  profile_scale=False)

# Optionally, un-standardize coefficients to compare with R directly
coefficients = lasso.params[1:] / scaler.scale_  # Scale back the coefficients for features
intercept = lasso.params[0] - np.dot(coefficients, scaler.mean_)  # Adjust intercept
print("Intercept:", intercept)
print("Coefficients:", coefficients)


'''
Test for heteroscedasticity
'''

from statsmodels.stats.diagnostic import het_breuschpagan
from statsmodels.stats.diagnostic import het_white


# Again, assuming 'model' is your fitted OLS model from statsmodels
bp_test = het_breuschpagan(ols_model.fit().resid, ols_model.fit().model.exog)

white_test = het_white(ols_model.fit().resid, ols_model.fit().model.exog)


labels = ['Lagrange multiplier statistic', 'p-value', 'f-value', 'f p-value']
print(dict(zip(labels, bp_test)))

labels = ['Test Statistic', 'Test Statistic p-value', 'F-Statistic', 'F-Test p-value']
print(dict(zip(labels, white_test)))