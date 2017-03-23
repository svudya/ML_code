import numpy as np 
import matplotlib.pyplot as plt

def step_gradient(thet, points,learning_rate):
	thet_grad = 0
	new_grad = 0
	N = float(len(points))
	for i in range(len(points)):
		y = points[i,0]
		x = points[i,1]
		if np.isnan(x) or np.isnan(y) :
			pass
		else :
			thet_grad += -1/N * (np.log(1+np.exp((-y)* thet * x))) 

	new_grad = thet - (learning_rate * thet_grad)

	return new_grad

def compute_y(theta, x_list):
	y_final= []
	for i in range(len(x_list)):
		y_final.append(1/(1+np.exp((-theta)*x_list[i])))
	return y_final

def gradient_descent_runner(thet, points, learning_rate, iterations):
	for i in range(iterations):
		theta = step_gradient(thet, np.array(points),learning_rate)
	return theta

def run():
	points = np.genfromtxt('./titanic_train.csv',delimiter=',',skip_header=1,usecols=(1,4))
	learning_rate = 0.0001
	thet = 0
	iterations = 1000
	x_list = []
	y_list = []

	num_iterations = 1000
	print "Logistic Regression"
	for i in range(len(points)):
		y = points[i,0]
		x = points[i,1]
		if np.isnan(x) or np.isnan(y) :
			pass
		else :
			x_list.append(x)
			y_list.append(y)
	print x_list
	print y_list

	theta = gradient_descent_runner(thet, points, learning_rate, iterations)
	plt.scatter(x_list,y_list)
	plt.plot(x_list, compute_y(theta, x_list))
	plt.show()

if __name__ == '__main__':
	run()