import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np
from pylab import *
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
ind = range(len(x))
width = 0.35

for values in ticketsByOwner:
	l = values.split()
	y.append(l[0])
	x.append(l[-2])

#fig = pl.figure()
ax = subplot(1,1,1)

yy = map(float, y)
#rect = ax.bar(ind, y)
ax.bar(range(len(x)), yy)
ax.set_xticklabels(x)
#xticks(range(len(x))+ width)

ax.set_ylabel('Completed # of Tickets')
ax.set_title('Completed Tickets by Owner')

# ax.bar(x,y)

plt.show()