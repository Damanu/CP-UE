#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def fweu(func,dx):
	N=len(func)
	fx=[]
	i=0
	while i<N-1:
		fx.append((func[i+1]-func[i])/dx)
		i+=1
	return fx		

def fbeu(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N:
		fx.append((func[i]-func[i-1])/dx)
		i+=1
	return fx		

def fzd(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N-1:
		fx.append((func[i+1]-func[i-1])/(2*dx))
		i+=1
	return fx		

def fzd2(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N-1:
		fx.append((func[i+1]-2*func[i]+func[i-1])/(dx**2))
		i+=1
	return fx		




def sd(func,func_real):	#standard deviation
	N=len(func)
	var=0	
	i=0
	while i < N:
		var+=(func[i]-func_real[i])**2
		i+=1
	return np.sqrt(var/N*1.)

def eu_int_fw(LU,U,dt):
	return (U + dt*LU)

def eu_int_impl(LU,U,dt): #only for harmonic oszi
		
	return ((U + dt*LU)/(1+dt**2)) #here LU is at next step

def leapfrog(LU,U,dt,i):
	return ((U[i-1]+2.*dt*LU[i]))

def main():
	T=100.
	N=10000
	dt=T/N
	print dt
	xaxe=np.linspace(0,T,N)
	v=[0.,-np.sin(dt)]
	x=[1.,-np.cos(dt)]
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
