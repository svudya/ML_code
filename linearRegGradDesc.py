from numpy import *
import matplotlib.pyplot as plt

def compute_error(b, m, points):
    totalError = 0
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        totalError += (y - (m*x + b)) ** 2
    return totalError / float(len(points))

def compute_y(b,m,xlist):
    yfinal=[]
    for i in range(len(xlist)):
        yfinal.append(m*xlist[i]+b)

    return yfinal

def step_gradient(b, m, points, learning_rate):
    b_gradient=0
    m_gradient=0
    ylist=[]
    xlist=[]
    N=float(len(points))
    for i in range(0, len(points)):
        x = points[i,0]
        y = points[i,1]
        ylist.append(y)
        xlist.append(x)
        b_gradient += -(2/N) * (y - ((m * x) + b))
        m_gradient += -(2/N) * x * (y - ((m * x) + b))
    new_b = b - (learning_rate * b_gradient)
    new_m = m - (learning_rate * m_gradient)
    return [new_b, new_m, ylist, xlist]


def gradient_descent_runner(points, b, m, learning_rate, iterations):
    b = b
    m = m
    for i in range(iterations):
        [b, m, ylist, xlist] = step_gradient(b, m, array(points), learning_rate)
    return [b, m, ylist, xlist]

def run():
    points = genfromtxt('./data.csv', delimiter=',')
    
    learning_rate=0.0001
    #y=mx+b
    initial_m=0
    initial_b=0
    num_iterations=1000
    print "Starting gradient descent at b = {0}, m = {1}, error = {2}".format(initial_b, initial_m, compute_error(initial_b, initial_m, points))
    print "Running...."
    [b,m,ylist,xlist] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
    print "After {0} iterations, b = {1}, m = {2}, error = {3}".format(num_iterations, b, m, compute_error(b, m, points))
    plt.scatter(xlist,ylist)
    plt.plot(xlist,compute_y(b,m,xlist))
    plt.show()

if __name__ == '__main__':
	run()
