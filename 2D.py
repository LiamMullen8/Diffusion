import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np

# creating a blank window
# for the animation
fig = plt.figure()
axis = plt.axes(xlim=(-100, 100),
                ylim=(-100, 100))

line, = axis.plot([], [], lw=2)


# what will our line dataset
# contain?
def init():
    line.set_data([], [])
    return line,


# initializing empty values
# for x and y co-ordinates
xdata, ydata = [0], [0]


# animation function
def animate(i):

	# t is a parameter which varies
	# with the frame number
	t = 0.1 * i

	# x, y values to be plotted

	r1 = np.random.uniform(0,1)
	r2 = np.random.uniform(0,1)
	
	if r1 < 0.5:
		x = (xdata[-1] - 1)
	elif r1 > 0.5:
		x = (xdata[-1] + 1)
	else:
		x = xdata[-1]

	if r2 < 0.5:
		y = (ydata[-1] - 1)
	elif r2 > 0.5:
		y = (ydata[-1] + 1)
	else:
		y = ydata[-1]

	# if x in xdata and y in ydata:
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


# calling the animation function
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=50, interval=20, blit=True)
plt.show()
# saves the animation in our desktop
anim.save('growingCoil.gif', writer='ffmpeg', fps=30)
