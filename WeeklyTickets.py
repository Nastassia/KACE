import matplotlib
import pylab as p
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

for values in ticketsByOwner:
	l = values.split()
	y.append(l[0])
	x.append(l[-2])

fig = p.figure()
ax = fig.add_subplot(1,1,1)

ax.bar(x,y)

p.show()