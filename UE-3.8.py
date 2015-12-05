#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def zdif2(u,dx,n,j,NX):	#central difference (1st derivation in space)
	
	jm1=(j-1+NX)%NX
	jm2=(j-2+NX)%NX
	jp1=(j+1)%NX
	jp2=(j+2)%NX
	ux=(u[n][jp1]-2*u[n][j]+u[n][jm1])/(dx**2.)
	return ux

def function(t,x):
	f=list(2./np.cosh(x-4*t))
	return f
def LAX_WENDROF_con(NX,NT,dx,dt,v):
	u=startcond(NX,NT,dx,dt)
	n=0
	while n<NT: 
		u.append([])
		j=0
		while j<NX:
			jm1=(j-1+NX)%NX
			jm2=(j-2+NX)%NX
			jp1=(j+1)%NX
			jp2=(j+2)%NX


			F=3*u[n][j]**2+zdif2(u,dx,n,j,NX)
			Fup=3*u[n][jp1]**2+zdif2(u,dx,n,jp1,NX)
			Fdo=3*u[n][jm1]**2+zdif2(u,dx,n,jm1,NX)
			

			Fup2=3*u[n][jp2]**2+zdif2(u,dx,n,jp2,NX)
			Fdo2=3*u[n][jm2]**2+zdif2(u,dx,n,jm2,NX)
			

			uright=(1/2.*(u[n][jp1]+u[n][j])-dt/(2.*dx)*(Fup-F))
			uleft=(1/2.*(u[n][j]+u[n][jm1])-dt/(2.*dx)*(F-Fdo))
			
			uright2=(1/2.*(u[n][jp2]+u[n][jp1])-dt/(2.*dx)*(Fup2-Fup))
			uleft2=(1/2.*(u[n][jm2]+u[n][jm1])-dt/(2.*dx)*(Fdo-Fdo2))
			
	
	
			Fup_=3*uright**2+(uright2-2*uright+uleft)/(dx**2.)
			Fdo_=3*uleft**2+(uright-2*uleft+uleft2)/(dx**2.)

			
			url_=(uright+uleft)/2.
			
			
			u[n+1].append(u[n][j]-dt/(dx)*(Fup_-Fdo_))
			j+=1
		n+=1
	return u


def startcond(NX,NT,dx,dt):
	u=[[]]
	j=-NX/2
	n=0
	while j<NX/2:
		u[0].append(2./np.cosh(j*dx))	# index 0 is time, 1 is position
		j+=1
	print len(u[0])
	return u


	
def main():
	T=0.1	#timeinterval
	X=20.	#spaceinterval
	NX=2000
	dx=X/float(NX)
	dt=0.001
	NT=int(T/dt)
	print "alph= ",dt/dx
	v=1.
	j=0
	n=0
	uwen=LAX_WENDROF_con(NX,NT,dx,dt,v)
	print uwen[1]
#	taxe=np.linspace(0,T,len(u))
#	plt.plot(xaxe,u[0],color='b')
#	plt.plot(xaxe,function(0.05,xaxe),color='y')
	xaxe=np.linspace(-X/2,X/2,NX)
	plt.plot(xaxe,uwen[1],color='b')
	plt.plot(xaxe,uwen[0],color='y')
	plt.plot(xaxe,function(1.,xaxe))
	plt.show()
if __name__=="__main__":
	main()
