import matplotlib.pyplot as plt
import numpy as np

D1=int(input("Enter 1D Lim:"))
D2=int(input("Enter 2D Lim:"))
D3=int(input("Enter 3D Lim:"))
D4=int(input("Enter 4D Lim:"))


# 1-D random walk
##############################################

def oneD(N):
	y = [0 for i in range(0,N)]
	
	for i in range(1,N):
		r = np.random.uniform(0,1)
		if r < 0.5:
			y[i]=y[i-1] - 1
		elif r > 0.5:
			y[i]=y[i-1] + 1
		else:
			y[i]=y[i-1]
	
	print(y)

	fig1 = plt.figure()
	plt.plot(y)
	fig1.show()

oneD(D1)
