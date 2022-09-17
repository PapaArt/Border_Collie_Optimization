from vpython import *
#Web VPython 3.2
tgraph = graph(title="My graph", xtitle="Time [s]", ytitle="y [m]")
f1 = gcurve(color=color.blue, label="no air resistance")
f2 = gcurve(color=color.red)
g = 9.8
v1 = 5
v2 = 4
y = 0
y2 = 0
t = 0
dt = 0.01

while y >= 0:
    v1 = v1-g*dt
    v2 = v2-g*dt
    y = y+v1*dt
    y2 = y2+v2*dt
    f1.plot(t, y)
    f2.plot(t, y2)
    t = t+dt