#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys



def fzd(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N-1:
		fx.append((func[i+1]-func[i-1])/(2*dx))
		i+=1
	return fx

def function(t,x):
	return(1/2.*(1-np.exp(-4.*np.pi**2*t)*np.cos(2.*np.pi*x)))

def main():
	u=[[]]
	T=0.05	#timeinterval
	X=1.	#spaceinterval
	NX=100
	dx=X/NX
	dt=dx**2/6.
#	dx=np.sqrt(dt*6)
	D=1.
	NT=int(T/dt)
#	NX=int(X/dx)
	j=0
	n=0
	print NT
	print NX
	while j<NX:
		u[0].append(1/2.*(1-np.cos(2*np.pi*dx*j)))	# index 0 is time, 1 is position
		j+=1
	n=0
	print len(u[0])
	while n<NT: #
		j=1
		print u[n]
		u.append([u[n][0]])	#lower boundary
		while j<NX-1:
			u[n+1].append(u[n][j]+D*dt/dx**2*(u[n][j+1]-2*u[n][j]+u[n][j-1]))
			j+=1
			print j
		u[n+1].append(u[n][NX])	#upper boundary
		print "u len: ",len(u[n+1])
		n+=1
	xaxe=np.linspace(0,X,len(u[NT-1]))
	print u
	taxe=np.linspace(0,T,len(u[0]))
	plt.plot(xaxe,u[0])
	plt.plot(xaxe,u[NT-1])
	plt.plot(xaxe,function(0.1,xaxe))
	plt.show()
if __name__=="__main__":
	main()
