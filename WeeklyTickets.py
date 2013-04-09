import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
import pylab as pl
import sys

filename = sys.argv[-1]

tickets = matplotlib.mlab.csv2rec(filename)

tickets = [sub_list[0] for sub_list in tickets]

ticketsByOwner = []

for x in tickets:
	if "of Owner Name: " in x:
		ticketsByOwner.append(x)

y = []
x = []
N = 6
#err = [2, 6, 1, 7, 8, 4]

ind = np.arange(N)
width = 0.35

for values in ticketsByOwner:
	l = values.split()
	y.append(l[0])
	x.append(l[-2])

fig = pl.figure()
ax = fig.add_subplot(1,1,1)

rect = ax.bar(ind, y, width)

ax.set_ylabel('Completed Tickets')
ax.set_title('Completed Tickets by Owner')

# ax.bar(x,y)

plt.show()