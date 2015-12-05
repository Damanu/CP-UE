#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def main(argv):
#dt <sqrt(8)/w
	w=float(argv[1])
	#y=float(argv[2])
	N=10000
	dt=np.sqrt(8.)/w
	T=float(argv[2])
	N=T/dt
	print dt
	v=[0]
	x=[1]
	i=0
	
	while i<N-1:
		v.append(v[i]+dt/6*(-w**2*x[i]-2*w**2*(v[i]-w**2*dt/2*x[i])-2*w**2*(v[i]-dt/2*w**2*(v[i]-w**2*dt/2*x[i]))-w**2*(v[i]-dt*w**2*(v[i]-dt/2*w**2*(v[i]-w**2*dt/2*x[i])))))
		x.append(x[i]+dt/6*(v[i]+2*(x[i]+dt/2*v[i])+2*(x[i]+dt/2*(x[i]+dt/2*v[i]))+x[i]+dt*(x[i]+dt/2*(x[i]+dt/2*v[i]))))
		i+=1
	xaxe=np.linspace(0,T,N)
	plt.plot(xaxe,v)
	plt.plot(xaxe,x)
	plt.show()	
if __name__=="__main__":
	main(sys.argv)
