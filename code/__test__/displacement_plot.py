from vpython import *
#Web VPython 3.2

tgraph = graph(xtitle="time", ytitle="Route[i]")
f1 = gdots(color=color.blue)

v1 = 5
acc = 9.8
t = 1
route = 0 
dt = 0.1

while route <= 100:
    v1 = sqrt(v1**2 + 2*acc*route)
    route = v1 * t + 1/2 * acc * t**2
    f1.plot(t, route)
    t = t + dt