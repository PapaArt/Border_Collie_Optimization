from vpython import *
#Web VPython 3.2
tgraph=graph(xtitle="x", ytitle="f(x)")
f1=gcurve(color=color.blue)

x=-3
dx=0.01
a=-2
da=0.01

fp=gdots(color=color.red, size=10)
data=[]
while x<3:
  fx=a*x**3-3
  f1.plot(x,fx)
  #data=data+[[x,fx]]
  x=x+dx
  
xt=-3
while xt<3:
  rate(100)
  fx=a*xt**3-3
  data=[[xt,fx]]
  fp.data=data
  xt=xt+dx