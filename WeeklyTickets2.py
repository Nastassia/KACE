import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import numpy as np
from pylab import *
import sys
import time
from datetime import date

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
width = 0.8
today = datetime.datetime.now()

for values in ticketsByOwner:
	l = values.split()
	y.append(l[0])
	x.append(l[-2])

#fig = pl.figure()
fig = Figure(figsize=[4,4])
ax = fig.add_subplot(1,1,1)

yy = map(float, y)
#rect = ax.bar(ind, y)
ax.bar(range(len(x)), yy, width, align='center', color='#159CD1')
ax.set_xticklabels(x)
ax.set_xticks(range(len(x)))
#xticks(range(len(x))+ width)

ax.set_ylabel('Completed # of Tickets')
ax.set_title('Completed Tickets by Owner')

canvas = FigureCanvas(fig)                                
canvas.print_figure(today.strftime("%Y-%m-%d"))

# ax.bar(x,y)

#plt.show()