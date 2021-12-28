import matplotlib.pyplot as plt
import numpy as np

D3=int(input("Enter 3D Lim:"))
def threeD(N):
	T=[[0,0,0] for i in range(0, N)]

	for i in range(1,N):
		x = np.random.uniform(0,1)
		y = np.random.uniform(0,1)
		z = np.random.uniform(0,1)

		if x<0.5:
			T[i][0] = T[i-1][0] - 1 
		elif x>0.5:
			T[i][0] = T[i-1][0] + 1
		else:
			T[i][0] = T[i-1][0]

		if y<0.5:
			T[i][1] = T[i-1][1] - 1 
		elif y>0.5:
			T[i][1] = T[i-1][1] + 1 
		else:
			T[i][1] = T[i-1][1] 

		if z<0.5:
			T[i][2] = T[i-1][2] - 1 
		elif z>0.5:
			T[i][2] = T[i-1][2] + 1 
		else:
			T[i][2] = T[i-1][2] 

	print(T)
	
	fig3 = plt.figure()
	ax = plt.axes(projection='3d')

	ax.plot3D([t[0] for t in T], [t[1] for t in T], [t[2] for t in T])
	fig3.show()

threeD(D3)
