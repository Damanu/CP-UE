#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def zdif(u,dx,n,j):	#central difference (1st derivation in space)
	ux=(u[n][j+1]-u[n][j-1])/(dx*2.)
	return ux

def function(t,x):
	f=(list(1/2.*(1.-np.cos(10.*np.pi*(x-t)))))
	i=0
	while i<len(x):
		if x[i]<=0.8:
			f[i]=0
		i+=1
	return f
def LAX_WENDROF_con(NX,NT,dx,dt,v,A):
	u=startcond(NX,NT,dx,dt,A)
	n=0
	while n<NT: 
		j=1
		u.append([1.])	#lower boundary
		while j<NX-1:
			
			F=u[n][j]/(2.*dx)*(u[n][j+1]-u[n][j-1])
			Fup=u[n][j+1]/(dx)*(u[n][j]-u[n][j-1])
			Fdo=u[n][j-1]/(2.*dx)*(u[n][j+1]-u[n][j])
			
			uright=(1/2.*(u[n][j+1]+u[n][j])-v*dt/(2.*dx)*(Fup-F))
			uleft=(1/2.*(u[n][j]+u[n][j-1])-v*dt/(2.*dx)*(F-Fdo))
			
			url_=(uright+uleft)/2.
			
			F_=url_/(2.*dx)*(uright-uleft)
			
			
			
#			uright=(1/2.*(u[n][j+1]+u[n][j])-v*dt/(2.*dx)*(u[n][j+1]-u[n][j]))
#			uleft=(1/2.*(u[n][j]+u[n][j-1])-v*dt/(2.*dx)*(u[n][j]-u[n][j-1]))
			u[n+1].append(u[n][j]-v*dt/dx*url_*(uright-uleft))
#			u[n+1].append(u[n][j]-v*dt/dx*(uright-uleft))
			j+=1
		u[n+1].append(u[n][0])	#upper boundary
#		u[n+1].append(u[n+1][NX-2]+3*u[n+1][NX-3]+u[n+1][NX-4])
		n+=1
	return u


def startcond(NX,NT,dx,dt,A):
	u=[[]]
	j=0
	n=0
	while j<NX:
		if dx*j>=0 and dx*j<=0.2:
			u[0].append(1+A/2.*(1.-np.cos(10.*np.pi*dx*float(j))))	# index 0 is time, 1 is position
		else:
			u[0].append(1.)	# index 0 is time, 1 is position
		j+=1
	return u
	
def main():
	T=0.8	#timeinterval
	X=1.	#spaceinterval
	NX=100
	dx=X/float(NX)
	dt=0.01
	D=1.
	NT=int(T/dt)
	v=1.
	A=0.05
	j=0
	n=0
	v=1.
	uwen=LAX_WENDROF_con(NX,NT,dx,dt,v,A)

#	taxe=np.linspace(0,T,len(u))
#	plt.plot(xaxe,u[0],color='b')
#	plt.plot(xaxe,function(0.05,xaxe),color='y')
	xaxe=np.linspace(0,X,NX)
	plt.plot(xaxe,uwen[NT-1])
	plt.plot(xaxe,uwen[0])
	plt.show()
if __name__=="__main__":
	main()
