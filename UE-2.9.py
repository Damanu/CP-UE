#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def main(argv):
	w=float(argv[1])
	N=100
	T=1.
	dt=T/N
	v=[0]
	x=[1]
	i=0
	while i<N-1:
		v_=(v[i]-w**2*dt*x[i])
		x_=(x[i]+dt*v[i])
		v.append(v[i]-w**2*dt*x_)
		x.append(x[i]+dt*v_)
		i+=1
	xaxe=np.linspace(0,T,N)
	plt.plot(xaxe,v)
	plt.plot(xaxe,x)
	plt.show()	
if __name__=="__main__":
	main(sys.argv)
