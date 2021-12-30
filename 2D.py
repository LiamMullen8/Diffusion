import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import random

def init():
    line.set_data([], [])
    return line,

# animation function
def animate(i):

	r1 = np.random.uniform(0,1)
	r2 = np.random.uniform(0,1)
	
	if r1 < 0.5:
		x = (xdata[-1] - 1)
	elif r1 > 0.5:
		x = (xdata[-1] + 1)
	# else:
	# 	x = xdata[-1]

	if r2 < 0.5:
		y = (ydata[-1] - 1)
	elif r2 > 0.5:
		y = (ydata[-1] + 1)
	# else:
	# 	y = ydata[-1]

	if (x,y) in finish_:
		raise Exception(f"TARGET HIT: {(x,y)}")

	print((x,y))

	for i, (x1,y1) in enumerate(zip(xdata,ydata)):

		if (x1, y1) == (x, y):
			print("REPEAT", (x1,y1))

			del xdata[i:]
			del ydata[i:]

			break

	xdata.append(x)
	ydata.append(y)

	line.set_data(xdata, ydata)

	return line,


if __name__ == "__main__":
	S = int(input("Input Grid Size: "))
	L = int(input("Number of Targets: "))

		# creating a blank window
	# for the animation
	fig = plt.figure()
	axis = plt.axes(xlim=(-S, S), ylim=(-S, S))

	line, = axis.plot([], [], lw=2)
	finish_ = []

	# initializing empty values
	# for x and y co-ordinates
	xdata, ydata = [0], [0]

	for i in range(L):
		r1 = random.randint(-S,S)
		r2 = random.randint(-S,S)
		finish_.append((r1,r2))
		finish = axis.plot(r1, r2, "r+")


	# calling the animation function
	anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=20, blit=True)
	plt.show()

	# saves the animation in our desktop
	anim.save('growingCoil.gif', writer='ffmpeg', fps=30)
