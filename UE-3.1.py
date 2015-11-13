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


def main():
	u=[[]]
	T=1.	#timeinterval
	X=10.	#spaceinterval
	dt=0.1
	dx=0.23
	D=1.
	NT=int(T/dt)
	NX=int(X/dx)
	j=0
	n=0
	while j<NX-1:
		u[0].append(np.sin(np.pi*dx*j))	# index 0 is time, 1 is position
	n=1
	while n<T-1: #
		j=0
		u.append([0])	#lower boundary
		while j<N-3:
			u[n].append(u[n][j+1]+D*dt/dx**2*(u[n][j+2]-2*u[n][j+1]+u[n][j]))
			j+=1
		u[n].append(0)	#upper boundary
		n+=1
	print NT
	print NX
if __name__=="__main__":
	main()
