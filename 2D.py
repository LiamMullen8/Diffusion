import matplotlib.pyplot as plt
import numpy as np

D2=int(input("Enter 2D Lim:"))
def twoD(N):
	T=[[0,0] for i in range(0, N)]

	for i in range(1,N):
		x = np.random.uniform(0,1)
		y = np.random.uniform(0,1)

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

	print(T)
	
	fig2 = plt.figure()
	plt.plot([t[0] for t in T], [t[1] for t in T])
	fig2.show()

twoD(D2)


############################################################
# Discrete Form of Probabilities in 2D
# #NEED TO MEMOIZE##

g_size=int(input("Enter Grid Size:"))
T_slice=int(input("Enter Time Slice:"))

Grid = [[[-1 for j in range(-g_size, g_size+1)] for i in range(-g_size, g_size+1)] for N in range(0, T_slice+1)]

def W(m,p,N):

	# probability of moving in each direction
	pl=pr=pu=pd=0.25

	# only location possible at time=0 is (0,0)
	if N==0:
		if m==0 and p==0:
			return 1.0
		else:
			return 0.0

	w = pr*W(m-1, p, N-1) + pr*W(m+1, p, N-1) + pu*W(m, p-1, N-1) + pd*W(m, p+1, N-1)
	return w

for T in range(0, T_slice+1):
	for i in range(-g_size, g_size+1):
		for j in range(-g_size, g_size+1):
			Grid[T][g_size - i][g_size - j] = W(i,j,T)

# ##########################
# setup 3d plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

x=[]

# get each x,y,z tuple to plot
# z is probability of being at coord (x,y)
for i in range(-g_size, g_size+1):
	for j in range(-g_size, g_size+1):
		l = [i, j, Grid[T_slice][g_size - i][g_size - j]]
		x.append(l)


x=np.array(x)
print(x)

ax.scatter3D(x[:,0],x[:,1], x[:,2])
fig.show()
