# -*- coding: utf-8 -*-
"""
Created on Sat Jul 01 21:36:06 2017

@author: Wenke Huang
"""

import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import scipy.stats as ss
import matplotlib.pyplot as plt

def ANOVA(model, X, y):
    SSR = ((model.predict(X)-y.mean())**2).sum()
    df_R = X.shape[1]
    MSR = SSR/df_R
    SSE = ((y-model.predict(X))**2).sum()
    df_E = X.shape[0]-X.shape[1]-1
    MSE = SSE/df_E
    F_stat = MSR/MSE
    p_of_F = ss.f.sf(F_stat, df_R, df_E)
    return({'SSR': SSR,
            'df_R': df_R,
            'MSR': MSR,
            'SSE': SSE,
            'df_E': df_E,
            'MSE': MSE,
            'F_stat': F_stat,
            'p_of_F': p_of_F})

def get_RMSE(model, X, y):
    resid = y-model.predict(X)
    RMSE = ((resid**2).mean())**.5
    return(RMSE)

## Not finished
def Summary(model, X, y):
    C_diag = np.diag(np.linalg.inv(np.dot(np.transpose(X), X)))
    if model.intercept_ != 0:
        se = (((y-model.predict(X))**2).sum()/(X.shape[0]-X.shape[1]-1))**.5
    else:
        se = (((y-model.predict(X))**2).sum()/(X.shape[0]-X.shape[1]))**.5
    se_beta = se*C_diag**.5
    t_stat = (model.coef_-0.0)/se_beta
    return(se_beta)

a = Summary(regr_1a, X_1a, y_1)
X_1a.shape[0]

# Question 1
## (a)
path = "C:/users/whuang67/downloads/nutrition.csv"
nutrition = pd.read_csv(path)
nutrition.drop(nutrition[['ID', 'Desc', 'Portion']], axis=1, inplace=True)
X_1a = nutrition.drop(nutrition[['Calories']], axis=1)
y_1 = nutrition.Calories
regr_1a = LinearRegression().fit(X_1a, y_1)
result_1a = ANOVA(regr_1a, X_1a, y_1)
print "F-stat is {}.".format(result_1a['F_stat'])
print "P-value is {}.".format(result_1a['p_value'])
    
## (b)
## (c)
X_1c = nutrition[['Carbs', 'Sodium', 'Fat', 'Protein']]
regr_1c = LinearRegression().fit(X_1c, y_1)
result_1c = ANOVA(regr_1c, X_1c, y_1)
print "F-stat is {}.".format(result_1c['F_stat'])
print "P-value is {}.".format(result_1c['p_value'])

## (d)
## (e)




# Question 2
## (a)
X_2a = nutrition[['Carbs', 'Fat', 'Protein']]
regr_2a = LinearRegression().fit(X_2a, y_1)
result_2a = ANOVA(regr_2a, X_2a, y_1)
print "F-stat is {}.".format(result_2a["F_stat"])
print "P-value is {}.".format(result_2a["p_value"])

## (b)
print(regr_2a.coef_)
print(regr_2a.intercept_)
## (c)
regr_2a.predict(pd.DataFrame({'Carbs': [47],
                              'Fat': [28],
                              'Protein': [25]}))
## (d)
regr_2a.predict(pd.DataFrame({'Carbs': [47],
                              'Fat': [28],
                              'Protein': [25]}))
## (e)
s_y = y_1.std()
s_e = (((y_1-regr_2a.predict(X_2a))**2).sum()/(X_2a.shape[0]-X_2a.shape[1]-1))**.5
print "s_y is {}.".format(s_y)
print "s_e is {}.".format(s_e)

## (f)
print "R^2 is {}.".format(regr_2a.score(X_2a, y_1))

## (g)





# Question 3
## (a)
path = "C:/users/whuang67/downloads/goalies_cleaned2015.csv"
goalies = pd.read_csv(path)
X_3a = goalies.drop(goalies[['W']], axis=1)
y_3 = goalies.W
regr3_full = LinearRegression().fit(X_3a, y_3)
result_3a = ANOVA(regr3_full, X_3a, y_3)
print "F-stat is {}.".format(result_3a['F_stat'])
print "P-value is {}.".format(result_3a['p_of_F'])

## (b)
RMSE_3b = get_RMSE(regr3_full, X_3a, y_3)
print "RMSE is of full model is {}.".format(RMSE_3b)

## (c)
X_3c = goalies[['GA', 'GAA', 'SV', 'SV_PCT']]
regr3_small = LinearRegression().fit(X_3c, y_3)
RMSE_3c = get_RMSE(regr3_small, X_3c, y_3)
print "RMSE of small model is {}.".format(RMSE_3c)

## (d)
X_3d = goalies[['GAA', 'SV_PCT']]
regr3_small2 = LinearRegression().fit(X_3d, y_3)
RMSE_3d = get_RMSE(regr3_small2, X_3d, y_3)
print "RMSE of small model is {}.".format(RMSE_3d)

## (e)
## (f)




# Question 4
## (a)
np.random.seed(42)
n = 25
x0 = np.array([1]*n)
x1 = np.random.uniform(0, 10, n)
x2 = np.random.uniform(0, 10, n)
x3 = np.random.uniform(0, 10, n)
x4 = np.random.uniform(0, 10, n)
X = np.column_stack((x0, x1, x2, x3, x4))
C = np.linalg.inv(np.dot(np.transpose(X), X))
y = np.array([0]*n)
ex_4_data = pd.DataFrame({"y": y,
                          "x1": x1,
                          "x2": x2,
                          "x3": x3,
                          "x4": x4})
print(np.diag(C))
print(ex_4_data[9:10])

## (b)
beta_hat_1 = []
beta_2_pval = []
beta_3_pval = []

## (c)
np.random.seed(42)
for i in range(0, 1500):
    X = ex_4_data[['x1', 'x2', 'x3', 'x4']]
    y = 2+3*X.x1+4*X.x2+X.x4+np.random.normal(0, 4, n)
    regr = LinearRegression().fit(X, y)
    beta_hat_1.append(regr.coef_[0])
    
## (d)
print np.mean(np.array(beta_hat_1))
print np.std(np.array(beta_hat_1), ddof=1)

## (e)
plt.hist(beta_hat_1, 25, normed=True)
fit_normal = ss.norm.pdf(sorted(beta_hat_1),
                         3,
                         (16*np.diag(C)[1])**.5)
plt.plot(sorted(beta_hat_1), fit_normal)
plt.show()

## (f)
## (g)