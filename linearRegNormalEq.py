import numpy as np

import matplotlib.pyplot as plt


def compute_error(b,m,points):
	totalError = 0
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,0]
		totalError += (y - (m*x + b)) ** 2
	return totalError/len(points)

def compute_y(b,m,xlist):
    yfinal=[]
    for i in range(len(xlist)):
        yfinal.append(m*xlist[i]+b)

    return yfinal

def run():
	X = []
	Y = []
	Xpoints = []
	Ypoints = []
	xMatrix = []
	yMatrix = []
	points = np.genfromtxt('./data.csv', delimiter=',')
	print "finding b and m through Normal equation method"
	
	for i in range(0, len(points)):
		x = points[i,0]
		y = points[i,1]
		Xpoints.append(x)
		Ypoints.append(y)
		X.append([1,x])
		Y.append([y])

	xMatrix = np.matrix(X)
	print "xMatrix"
	print xMatrix
	print np.shape(xMatrix)

	yMatrix = np.matrix(Y)
	print "yMatrix"
	print yMatrix
	print np.shape(yMatrix)

	xTranspose = xMatrix.transpose()
	print "xTranspose"
	print xTranspose
	print np.shape(xTranspose)

	xTx = np.matmul(xTranspose, xMatrix)
	print "x transpose x"
	print xTx
	print np.shape(xTx)

	xTxInv = np.linalg.inv(xTx)
	print "x transpose x inverse"
	print xTxInv
	print np.shape(xTxInv)

	xTxInvxT = np.matmul(xTxInv ,xTranspose)
	print "x transpose x Inverse X transpose"
	print xTxInvxT
	print np.shape(xTxInvxT)

	theta = np.matmul(xTxInvxT, yMatrix)
	print "theta"
	print theta

	plt.scatter(Xpoints,Ypoints)
	plt.plot(Xpoints, compute_y(theta[0,0], theta[1,0], Xpoints))
	plt.show()



if __name__ == '__main__':
	run()