#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def eu_int_fw(LU,U,dt):
	return (U + dt*LU)

def eu_int_impl(LU,U,dt): #only for harmonic oszi
		
	return ((U + dt*LU)/(1+dt**2)) #here LU is at next step

def leapfrog(LU,U,dt,i):
	return ((U[i-1]+2.*dt*LU[i]))

def eu_impl_2 (LU,U,dt,i):
	return (U[i]-dt/2*(LU[i]+LU[i+1]))

def main(argv):
	print argv[1]
	N=100
	T=14.
	dt=T/N
	
	print dt
	xaxe=np.linspace(0,T,N)
	ddt=0.
	if argv[1]=="1":
		v=[0.]
		x=[1.]
		i=0
		while i<N-1:
			v.append((v[i]-dt*x[i])/(1+dt**2))
			x.append(x[i]+dt*v[i+1])
			i+=1
	elif argv[1]=="2":
		v=[0.,-np.sin(dt)]
		x=[1.,np.cos(dt)]
		i=1
		while i<N-1:
			v.append(v[i-1]-2*dt*x[i])
			x.append(x[i-1]+2*dt*v[i])
			i+=1
	elif argv[1]=="3":
		v=[0.]
		x=[1.]
		i=0
		while i<N-1:
			v.append((v[i]-dt*x[i]+dt**2/4.*v[i])/(1.-dt**2/4))
			x.append(x[i]-dt*(v[i]+v[i+1]))	
			i+=1
	else:
		print "error"
		sys.exit()
	plt.plot(xaxe,v)
	plt.plot(xaxe,x)
	plt.show()


if __name__=="__main__":
	main(sys.argv)
