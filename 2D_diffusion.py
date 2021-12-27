
# Discrete Form
def W(m,p,N):
	# probability of moving in each direction
	pl=pr=pu=pd=0.25

	if N==0:
		if m==0 and p==0:
			return 1
		else:
			return 0
	
	w = pr*W(m-1, p, N-1) + pr*W(m+1, p, N-1) + pu*W(m, p-1, N-1) + pd*W(m, p+1, N-1)

	return w


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

print(W(0,0,1))
print(W(1,0,1))
print(W(0,1,1))
print(W(1,1,2))
