import pandas as pd 
import numpy as np 
import statsmodels.api as sm
import statsmodels.stats.api as sms
from glmnet import ElasticNet as EN
from sklearn.linear_model import ElasticNet
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt
import seaborn as sns
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.metrics import mean_squared_error, r2_score


def custom_scaler(X):
    X_std = (X - X.min()) / (X.max() - X.min())
    return X_std

def custom_normal(X):
    X_std = (X - X.mean())/ X.std()
    return X_std

df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')
normal_df = pd.read_csv('https://raw.githubusercontent.com/jww2145/free-trade-agreements/main/data-exploration/time_series/time-series-data.csv')
standard_df = normal_df.copy()  # Create a separate copy for standardization
columns_to_scale = ['IMPGS', 'INTDSRUSM193N', 'New House Sale', 'S&P Returns', 'UNRATE', 'WM2NS', 'GDPC1', 'T10Y2Y', 'CORESTICKM159SFRBATL', 'DEXCHUS', 'DEXCAUS']


for x in columns_to_scale:
    normal_df[x] = custom_normal(df[x])
    standard_df[x] = custom_scaler(df[x])


data_standard = standard_df[(standard_df['Year'] >= 1991)].reset_index()
data_normal = normal_df[(normal_df['Year'] >= 1991)].reset_index()

back_testing = standard_df[(standard_df['Year'] < 1991)].reset_index()

X_new = back_testing[['New House Sale', 'T10Y2Y', 'S&P Returns', 'DEXCHUS', 'UNRATE', 'DEXCAUS']].copy()
y_new = back_testing['IMPGS']

X_new = sm.add_constant(X_new)


#Standardized OLS
y_min_max = data_standard['IMPGS'].copy()
X_min_max = data_standard[['New House Sale', 'T10Y2Y', 'S&P Returns', 'DEXCHUS', 'UNRATE', 'DEXCAUS']].copy()


''' ADF TEST

for i,column in enumerate(X_min_max):
    if(i != 0):
        result = adfuller(X_min_max[column], maxlag= 3, autolag=None, regression="ct")
        print(f'ADF Statistic for {column}: %f' % result[0])
        print('p-value: %f' % result[1])
'''   

impgs_diff = np.diff(y_min_max)
y_min_max = np.append([0],impgs_diff)

house_diff = np.diff(X_min_max['New House Sale'])
X_min_max['New House Sale'] = np.append([0],house_diff)

t10_diff = np.diff(X_min_max['T10Y2Y'])
X_min_max['T10Y2Y'] = np.append([0],t10_diff)

sp_diff = np.diff(X_min_max['S&P Returns'])
X_min_max['S&P Returns'] = np.append([0],sp_diff)

dexchus_diff = np.diff(X_min_max['DEXCHUS'])
X_min_max['DEXCHUS'] = np.append([0],dexchus_diff)

unrate_diff = np.diff(X_min_max['UNRATE'])
X_min_max['UNRATE'] = np.append([0], unrate_diff)

dexcaus_diff = np.diff(X_min_max['DEXCAUS'])
X_min_max['DEXCAUS'] = np.append([0],dexcaus_diff)

X_min_max = sm.add_constant(X_min_max)

standardized_ols = sm.OLS(y_min_max,X_min_max).fit()
names = names = ['Lagrange multiplier statistic', 'p-value',
         'f-value', 'f p-value']
test_result = sms.het_breuschpagan(standardized_ols.resid, standardized_ols.model.exog)

#print("Test Results for BP: ", test_result)
#print(standardized_ols.summary())

y_pred = standardized_ols.predict(X_new)

mse = mean_squared_error(y_new, y_pred)
r2 = r2_score(y_new, y_pred)

#print(f'Mean Squared Error: {mse}')
#print(f'R-squared: {r2}')

#Normalized OLS
y_normalized = data_normal['IMPGS'].copy()
X_normalized = data_normal[['New House Sale', 'T10Y2Y', 'S&P Returns', 'DEXCHUS', 'UNRATE', 'DEXCAUS']].copy()




'''ADF TEST 
for i,column in enumerate(X_normalized):
    if(i != 0):
        result = adfuller(X_normalized[column], maxlag= 3, autolag=None, regression="ct")
        print(f'ADF Statistic for {column}: %f' % result[0])
        print('p-value: %f' % result[1])
'''

impgs_diff = np.diff(y_normalized)
y_normalized = np.append([0],impgs_diff)

house_diff = np.diff(X_normalized['New House Sale'])
X_normalized['New House Sale'] = np.append([0],house_diff)

t10_diff = np.diff(X_normalized['T10Y2Y'])
X_normalized['T10Y2Y'] = np.append([0],t10_diff)

sp_diff = np.diff(X_normalized['S&P Returns'])
X_normalized['S&P Returns'] = np.append([0],sp_diff)

dexchus_diff = np.diff(X_normalized['DEXCHUS'])
X_normalized['DEXCHUS'] = np.append([0],dexchus_diff)

unrate_diff = np.diff(X_normalized['UNRATE'])
X_normalized['UNRATE'] = np.append([0], unrate_diff)

dexcaus_diff = np.diff(X_normalized['DEXCAUS'])
X_normalized['DEXCAUS'] = np.append([0],dexcaus_diff)
        
X_normalized = sm.add_constant(X_normalized)

normalized_ols = sm.OLS(y_normalized,X_normalized).fit()
names = names = ['Lagrange multiplier statistic', 'p-value',
         'f-value', 'f p-value']
test_result2 = sms.het_breuschpagan(normalized_ols.resid, normalized_ols.model.exog)

#print("Test for BP: ", test_result2)
print(normalized_ols.summary())


'''VIF TEST

vif_data = pd.DataFrame()
vif_data["feature"] = X_min_max.columns

# Calculating VIF for each feature
vif_data["VIF"] = [variance_inflation_factor(X_min_max.values, i) for i in range(X_min_max.shape[1])]

print(vif_data)
'''


'''RESIDUAL PLOTS

residuals = standardized_ols.resid
fitted_values = standardized_ols.fittedvalues


plt.figure(figsize=(10, 6))
sns.residplot(x=fitted_values, y=residuals**2,color="g", scatter_kws={'alpha': 0.5})
plt.xlabel('Predicted Value')
plt.ylabel('Residuals-squared')
plt.title(f'Residual Plot')
plt.grid(True)
plt.show()
'''

#WLS 

residuals = standardized_ols.resid
predictor = X_min_max['S&P Returns']
predictor = sm.add_constant(predictor)


# Estimate the variance function using squared residuals
variance_model = sm.OLS(abs(residuals), predictor).fit()

#print(variance_model.summary())
weights = 1 / (variance_model.fittedvalues**2)

wls_model = sm.WLS(y_min_max,X_min_max,weights).fit()


#print(wls_model.summary())

#GLS Model 

sigma = np.cov(np.sqrt(residuals**2))
gls_model = sm.GLS(y_min_max,X_min_max,sigma).fit()

#print(gls_model.summary())


#LASSO 

cv_model = EN(alpha = 1)
cv_model.fit(X_min_max, y_min_max)

print(cv_model.lambda_best_)

model = ElasticNet(l1_ratio=1, alpha = 0.00682454)
model.fit(X_min_max,y_min_max)
coefficients = pd.DataFrame(model.coef_, index=X_min_max.columns, columns=['Coefficient'])

print(coefficients)
