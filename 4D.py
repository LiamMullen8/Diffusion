import matplotlib.pyplot as plt
import numpy as np

D4=int(input("Enter 4D Lim:"))
def fourD(N):
	T=[[0,0,0,0] for i in range(0, N)]

	for i in range(1,N):
		x = np.random.uniform(0,1)
		y = np.random.uniform(0,1)
		z = np.random.uniform(0,1)
		w = np.random.uniform(0,1)

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

		if w<0.5:
			T[i][3] = T[i-1][3] - 1 
		elif w>0.5:
			T[i][3] = T[i-1][3] + 1 
		else:
			T[i][3] = T[i-1][3] 

	print(T)
	
	fig4 = plt.figure()
	ax = plt.axes(projection='3d')

	i = ax.scatter([t[0] for t in T], [t[1] for t in T], [t[2] for t in T], s=[abs(10*t[3]) for t in T])
	ax.plot3D([t[0] for t in T], [t[1] for t in T], [t[2] for t in T])

	fig4.show()

fourD(D4)
