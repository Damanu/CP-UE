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
	return (U[i]+dt/2*(LU[i]+LU[i+1])

def main():
	T=10.
<<<<<<< HEAD
	N=10000
=======
	N=1000
>>>>>>> 1621e0da9bea4419785a48453779cd0e41429d9c
	dt=T/N
	print dt
	xaxe=np.linspace(0,T,N)
	v=[0.,-np.sin(dt)]
	x=[1.,np.cos(dt)]
	i=1	
	ddt=0.
	while i<N-1:
	#	v.append(eu_int_impl(v[i],-x[i],dt))
	#	x.append(eu_int_fw(x[i], v[i+1],dt))
		v.append(leapfrog(v,x,-dt,i))
		x.append(leapfrog(x,v,dt,i))
		i+=1
	plt.plot(xaxe,v)
	plt.plot(xaxe,x)
	plt.show()


if __name__=="__main__":
	main()
