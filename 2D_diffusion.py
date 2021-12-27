
g_size=int(input("Enter Grid Size:"))
T_slice=int(input("Enter Time Slice:"))

# this is so we can reference negatives
Grid = [[[0.0 for j in range(-g_size, g_size+1)] for i in range(-g_size, g_size+1)] for N in range(0, T_slice+1)]
print(Grid)
print("+++++++++++++++++++++++++++++++\n")

# Discrete Form
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

print(Grid)

























# Continuous Form
def U(x,y,t):

	pl=pr=pu=pd=0.25
	dx=dy=dt=1

	if t==0:
		if x==0 and y==0:
			return 1
		else:
			return 0
	u = pr*U(x-dx, y, t-dt) + pr*U(x+dx, y,  t-dt) + pu*U(x, y-dy,  t-dt) + pd*U(x, y+dy,  t-dt)

	return u
