#https://machinelearningmastery.com/arima-for-time-series-forecasting-with-python/
import pandas as pd
from pandas import read_csv
from pandas import datetime
from matplotlib import pyplot
import os
import shutil

#Change newid for 2 column data.
from myfunctions import newid2

def parser(x):
	return datetime.strptime('190'+x, '%Y-%m')

series = read_csv(newid2, index_col=0, squeeze=True)

series.tail(300)
print(series.head())
series.plot()
#pyplot.show()

##############AutoCorrelations###################

from pandas.plotting import autocorrelation_plot
autocorrelation_plot(series)
#pyplot.show()

####################ARIMA##########################

from pandas import DataFrame
from statsmodels.tsa.arima_model import ARIMA
from pandas.plotting import autocorrelation_plot

model = ARIMA(series, order=(5,1,0))
model_fit = model.fit(disp=0)
print(model_fit.summary())

# plot residual errors
residuals = DataFrame(model_fit.resid)
residuals.plot()
#pyplot.show()
residuals.plot(kind='kde')
#pyplot.show()
print(residuals.describe())

######################Future Timesteps#########################

from sklearn.metrics import mean_squared_error

X = series.values
size = int(len(X) * 0.66)
train, test = X[0:size], X[size:len(X)]
history = [x for x in train]
predictions = list()
for t in range(len(test)):
	model = ARIMA(history, order=(5,1,0))
	model_fit = model.fit(disp=0)
	output = model_fit.forecast()
	yhat = output[0]
	predictions.append(yhat)
	obs = test[t]
	history.append(obs)
	print('predicted=%f, expected=%f' % (yhat, obs))
error = mean_squared_error(test, predictions)
print('Test MSE: %.3f' % error)
# plot
pyplot.plot(test)
pyplot.plot(predictions, color='red')
#pyplot.show()

from myfunctions import mywith
from myfunctions import newsummary

with open(mywith, 'w') as f:
    print(newsummary, 'predicted=%f, expected=%f' % (yhat, obs), file=f)  
    print('', file=f) 	
    print('Summary ARIMA results', model_fit.summary(), file=f) 
    print('', file=f) 
    print('Summary ARIMA Residuals', residuals.describe(), file=f) 


from myfunctions import shutil1, shutil2, shutil3, shutil4, shutil5

shutil.copy(shutil1, shutil2)
shutil.move(shutil1, shutil3)
shutil.move(shutil4, shutil5)
