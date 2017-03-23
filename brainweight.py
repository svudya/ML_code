import pandas as pa
from sklearn import linear_model
import matplotlib.pyplot as plt

dataframe = pa.read_fwf('linear_regression_demo/brain_body.txt')
x_values = dataframe[['Brain']]
y_values = dataframe[['Body']]

bodyreg = linear_model.LinearRegression()
bodyreg.fit(x_values,y_values)
print "x_values"
print x_values
print "y_values"
print y_values

predict = 0
predict = bodyreg.predict(x_values)
print predict
plt.scatter(x_values, y_values)
plt.plot(x_values, predict)
plt.show()
