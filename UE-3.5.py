#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def disp(dt,dx,v,k):
	w=np.log(1-1.0j*v*dt/dx*np.sin(k*dx))/(1.0j*dt)
	return w

def disp_lax(dt,dx,v,k):
	w=np.log(np.cos(k*dx)-1.0j*v*dt/dx*np.sin(k*dx))/(1.0j*dt)
	return w

def disp_analyt(v,k):
	w=v*k
	return w

def main():
	v=1.
	dx=1.
	dt=1.
	k=np.linspace(0,np.pi,1000)
	v=0.25
	while v<=1:	
		a=v*dt/dx
		w=disp(dt,dx,v,k)*dt/a
		w_=disp_analyt(v,k)*dt/a
		plt.subplot(1,2,1)
		plt.plot(k,(w.real),color='r')
		plt.plot(k,disp_analyt(v,k),color='b')
		plt.subplot(1,2,2)
		plt.plot(k,(w.imag))
		plt.plot(k,(disp_analyt(v,k).imag))
		v+=0.25
	plt.show()
if __name__=="__main__":
	main()
