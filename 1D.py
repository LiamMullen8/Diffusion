import matplotlib.pyplot as plt
import numpy as np

# 1-D random walk
##############################################

def oneD():
	global y
	
	for i in range(1, len(y)):
		r = np.random.uniform(0,1)
		if r < 0.5:
			y[i]=y[i-1] - 1
		elif r > 0.5:
			y[i]=y[i-1] + 1
		# else:
		# 	y[i]=y[i-1]
	# print(y)


def W(m,N):

	# probability of moving in each direction
	pl=pr=0.5

	# only location possible at time=0 is (0,0)
	if N==0:
		if m==0:
			return 1.0
		else:
			return 0.0

	w = pr*W(m-1, N-1) + pl*W(m+1, N-1)
	return w

############################################################
# Discrete Form of Probabilities in 1D
# #NEED TO MEMOIZE##
if __name__ == "__main__":

	D1=int(input("Enter 1D Lim:"))
	T_slice=int(input("Enter Time Slice:"))
	# if(T_slice >= D1):
	# 	raise Exception("Time slice must be within your specified range")
	
	y = [0 for _ in range(0, max(D1,T_slice+1))]
	oneD()

	fig, axs = plt.subplots(2)

	axs[0].set_title("1D Random Walk")
	axs[0].plot(y)
	axs[0].plot(T_slice, y[T_slice], 'rx')

	axs[1].set_title(f"Probability of being @ y = {y[T_slice]} for t = {T_slice}")
	axs[1].axvline(x=y[T_slice], color='r')

	###############	###############	###############

	Grid = [[-1 for _ in range(-D1, D1+1)] for _ in range(0, T_slice+1)]

	for T in range(0, T_slice+1):
		for i in range(-D1, D1+1):
				Grid[T][D1 - i] = W(i,T)


	x=[]
	# y is probability of being at coord (x)
	for i in range(-D1, D1+1):
			l = [i, Grid[T_slice][D1 - i]]
			x.append(l)

	x = np.array(x)
	print(x)

	axs[1].plot(x[:,0], x[:,1])

	fig.show()

