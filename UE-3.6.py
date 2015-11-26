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
	f=(list(1/2.*(1.-np.cos(10.*np.pi*(x-t)))))
	i=0
	while i<len(x):
		if x[i]<=0.8:
			f[i]=0
		i+=1
	return f
def zdiff(u,j,n,dx):
	return(1./dx**2*(u[n][j+1]-2*u[n][j]+u[n][j-1]))


def updiff(u,j,n,dx):
	return(1./(2.*dx)*(u[n][j]-u[n][j-1]))

def UPWIND(NX,NT,dx,dt,v):
	u=startcond(NX,NT,dx,dt)
	n=0
	while n<NT: #
		j=1
		u.append([0])	#lower boundary
		while j<NX:
			u[n+1].append(u[n][j]-v*dt*updiff(u,j,n,dx))
			j+=1
#		u[n+1].append(u[n][NX-1])	#upper boundary
		n+=1
	return u

def LAX(NX,NT,dx,dt,v):
	u=startcond(NX,NT,dx,dt)
	n=0
	while n<NT: #
		j=1
		u.append([0])	#lower boundary
		while j<NX-1:
			u[n+1].append(1/2.*(u[n][j+1]+u[n][j-1])-v*dt/(2.*dx)*(u[n][j+1]-u[n][j-1]))
			j+=1
		u[n+1].append(2*u[n+1][NX-2]+3*u[n+1][NX-3]+u[n+1][NX-4])	#upper boundary
		n+=1
	return u

def LAX_WENDROF(NX,NT,dx,dt,v):
	u=startcond(NX,NT,dx,dt)
	n=0
	while n<NT: #
		j=1
		u.append([0])	#lower boundary
		while j<NX-1:
			uright=(1/2.*(u[n][j+1]+u[n][j])-v*dt/(2.*dx)*(u[n][j+1]-u[n][j]))
			uleft=(1/2.*(u[n][j]+u[n][j-1])-v*dt/(2.*dx)*(u[n][j]-u[n][j-1]))
			u[n+1].append(u[n][j]-v*dt/dx*(uright-uleft))
			j+=1
		u[n+1].append(2*u[n+1][NX-2]+3*u[n+1][NX-3]+u[n+1][NX-4])	#upper boundary
		n+=1
	return u


def startcond(NX,NT,dx,dt):
	u=[[]]
	j=0
	n=0
	while j<NX:
		if dx*j>=0 and dx*j<=0.2:
			u[0].append(1./2.*(1.-np.cos(10.*np.pi*dx*float(j))))	# index 0 is time, 1 is position
		else:
			u[0].append(0.)	# index 0 is time, 1 is position
		j+=1
	return u
	
def main():
	T=0.8	#timeinterval
	X=1.	#spaceinterval
	NX=1000
	dx=X/NX
	dt=0.001
	D=1.
	NT=int(T/dt)
	v=1.

	j=0
	n=0
	v=1
	while dt<=0.001:	
		uup=UPWIND(NX,NT,dx,dt,v)
		ulax=LAX(NX,NT,dx,dt,v)
		uwen=LAX_WENDROF(NX,NT,dx,dt,v)
		xaxe=np.linspace(0,X,len(uup[0]))
		f=function(0.8,xaxe)
		plt.subplot(3,1,1)
		plt.title("upwind")
		plt.plot(xaxe,f,color='y')
		plt.plot(xaxe,uup[NT-1])
		plt.subplot(3,1,2)
		plt.title("lax")
		plt.plot(xaxe,f,color='y')
		plt.plot(xaxe,ulax[NT-1])
		plt.subplot(3,1,3)
		plt.title("lax-wendrof")
		plt.plot(xaxe,f,color='y')
		plt.plot(xaxe,uwen[NT-1])
		dt+=0.0005


#	taxe=np.linspace(0,T,len(u))
#	plt.plot(xaxe,u[0],color='b')
#	plt.plot(xaxe,function(0.05,xaxe),color='y')
	plt.show()
if __name__=="__main__":
	main()
