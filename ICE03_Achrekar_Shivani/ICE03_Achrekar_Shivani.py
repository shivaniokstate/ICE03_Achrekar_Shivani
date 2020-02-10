import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

#For QQ Plot
import scipy.stats as sts

#Correlation p-values
from scipy.stats.stats import pearsonr

#Regression output
from sklearn.linear_model import LinearRegression
import statsmodels.formula.api as smf
from statsmodels.graphics.regressionplots import *



dir = r'C:\Users\shivani\source\repos\msis5223-pds2-master\ice-regression-shivaniokstate\data'

os.chdir(dir)

os.getcwd()

reduction_data = pd.read_table('reduction_data_new.txt')
reduction_data.columns
reduction_data.dtypes

##linearity
reduction_data.plot.scatter(x='time', y='intent01')
reduction_data.plot.scatter(x='operatingsys', y='intent01')
reduction_data.plot.scatter(x='race_white', y='intent01')
reduction_data.plot.scatter(x='peruse03', y='intent01')
reduction_data.plot.scatter(x='pereou06', y='intent01')

reduction_data.corr()

##colinearity
pearsonr(reduction_data.time, reduction_data.intent01)
pearsonr(reduction_data.operatingsys, reduction_data.intent01)
pearsonr(reduction_data.race_white, reduction_data.intent01)
pearsonr(reduction_data.peruse03, reduction_data.intent01)
pearsonr(reduction_data.pereou06, reduction_data.intent01)

# Use the sklearn library for regression
linreg1 = LinearRegression(fit_intercept=True, normalize=True)
linreg1.fit(reduction_data[['time','operatingsys','race_white','peruse03','pereou06']],reduction_data.intent01)

#Calculate VIF for Radiation
linreg1.fit(reduction_data[['time','operatingsys','peruse03','pereou06']],reduction_data.race_white)
vif1 = 1/(1 - linreg1.score(reduction_data[['time','operatingsys','peruse03','pereou06']],reduction_data.race_white))

#Calculate VIF for Wind
linreg1.fit(reduction_data[['time','race_white','peruse03','pereou06']],reduction_data.operatingsys)
vif2 = 1/(1 - linreg1.score(reduction_data[['time','race_white','peruse03','pereou06']],reduction_data.operatingsys))

#Calculate VIF for Temperature
linreg1.fit(reduction_data[['operatingsys','race_white','peruse03','pereou06']],reduction_data.time)
vif3 = 1/(1 - linreg1.score(reduction_data[['operatingsys','race_white','peruse03','pereou06']],reduction_data.time))

linreg1.fit(reduction_data[['operatingsys','race_white','time','pereou06']],reduction_data.peruse03)
vif4 = 1/(1 - linreg1.score(reduction_data[['operatingsys','race_white','time','pereou06']],reduction_data.peruse03))

linreg1.fit(reduction_data[['operatingsys','race_white','peruse03','time']],reduction_data.pereou06)
vif5 = 1/(1 - linreg1.score(reduction_data[['operatingsys','race_white','peruse03','time']],reduction_data.pereou06))

#Output VIF scores
print('VIF race_white: ', vif1,
        '\nVIF operatingsys: ', vif2,
        '\nVIF time: ', vif3,
        '\nVIF peruse03: ', vif4,
        '\nVIF pereou06: ', vif5)

##homoscedasticity
linreg2 = smf.ols('intent01 ~ time + operatingsys + race_white + peruse03 + pereou06', reduction_data).fit()

#Assess homoscedasticity
plt.scatter(linreg2.fittedvalues, linreg2.resid)
plt.xlabel('Predicted/Fitted Values')
plt.ylabel('Residual Values')
plt.title('Assessing Homoscedasticity')
plt.plot([-40, 120],[0, 0], 'red', lw=2)   #Add horizontal line
plt.show()


##regression model
linreg2.summary()

##independence
sts.probplot(linreg2.resid, dist="norm", plot=plt)

##normality
plot_leverage_resid2(linreg2)

