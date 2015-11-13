#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def main(argv):
	w=float(argv[1])
	y=float(argv[2])
	N=10000
	T=20.
	dt=T/N
	print dt
	v=[0]
	x=[1]
	i=0
	while i<N-1:
		v.append(v[i]*(1-y*dt)-w**2*dt*x[i])
		x.append(x[i]+dt*v[i])
		i+=1
	xaxe=np.linspace(0,T,N)
	plt.plot(xaxe,v)
	plt.plot(xaxe,x)
	plt.show()	
if __name__=="__main__":
	main(sys.argv)
