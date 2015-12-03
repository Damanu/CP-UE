#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def zdif2(u,dx,n,j):	#central difference (1st derivation in space)
	ux=(u[n][j+1]-2*u[n][j]+u[n][j-1])/(dx**2.)
	return ux

def function(t,x):
	f=(list(1/2.*(1.-np.cos(10.*np.pi*(x-t)))))
	i=0
	while i<len(x):
		if x[i]<=0.8:
			f[i]=0
		i+=1
	return f
def LAX_WENDROF_con(NX,NT,dx,dt,v):
	u=startcond(NX,NT,dx,dt)
	n=0
	while n<NT: 
		j=3
		u.append([1.])	#lower boundary
		u[n].insert(NX,u[n][1])
		u[n].insert(NX+1,u[n][2])
		u[n].insert(0,u[n][NX-2])
		u[n].insert(NX+1,u[n][NX-3])
		print len(u[n])
		while j<NX-1:
#			if j<=1:
#				u[n].insert(0,u[n][NX-2])
#				
#				F=3*u[n][j+1]**2+zdif2(u,dx,n,j+1)
#				Fup=3*u[n][j+2]**2+zdif2(u,dx,n,j+2)
#				Fdo=3*u[n][j]**2+zdif2(u,dx,n,j)
#				
#				u[n].insert(0,u[n][NX-2])
#				Fup2=3*u[n][j+2]**2+zdif2(u,dx,n,j+2)
#				Fdo2=3*u[n][j]**2+zdif2(u,dx,n,j)
#				
#				u[n].pop(0)
#				u[n].pop(0)
#			elif j>=NX-2:
#				u[n].insert(NX,u[n][1])
#				F=3*u[n][j]**2+zdif2(u,dx,n,j)
#				Fup=3*u[n][j+1]**2+zdif2(u,dx,n,j+1)
#				Fdo=3*u[n][j-1]**2+zdif2(u,dx,n,j-1)
#				
##				u[n].insert(NX+1,u[n][2])
#
#				Fup2=3*u[n][j+2]**2+zdif2(u,dx,n,j+2)
#				Fdo2=3*u[n][j]**2+zdif2(u,dx,n,j)
#
###				u[n].pop()
#				u[n].pop()
#			else:
			F=3*u[n][j]**2+zdif2(u,dx,n,j)
			Fup=3*u[n][j+1]**2+zdif2(u,dx,n,j+1)
			Fdo=3*u[n][j-1]**2+zdif2(u,dx,n,j-1)
			
#				u[n].insert(NX,u[n][1])

			Fup2=3*u[n][j+2]**2+zdif2(u,dx,n,j+2)
			Fdo2=3*u[n][j-2]**2+zdif2(u,dx,n,j-2)
			
#				u[n].pop()

			Fup=u[n][j+1]/(dx)*(u[n][j]-u[n][j-1])
			Fdo=u[n][j-1]/(2.*dx)*(u[n][j+1]-u[n][j])
			uright=(1/2.*(u[n][j+1]+u[n][j])-dt/(2.*dx)*(Fup-F))
			uleft=(1/2.*(u[n][j]+u[n][j-1])-v*dt/(2.*dx)*(F-Fdo))
			
			uright2=(1/2.*(u[n][j+2]+u[n][j+1])-dt/(2.*dx)*(Fup2-Fup))
			uleft2=(1/2.*(u[n][j-1]+u[n][j-2])-v*dt/(2.*dx)*(Fdo-Fdo2))
			
	
	
			Fup_=3*uright**2+(uright2-2*uright+uleft)/(dx**2.)
			Fdo_=3*uleft**2+(uright-2*uleft+uleft2)/(dx**2.)

			
			url_=(uright+uleft)/2.
			
#			F_=url_/(2.*dx)*(uright-uleft)
			
			
#			uright=(1/2.*(u[n][j+1]+u[n][j])-v*dt/(2.*dx)*(u[n][j+1]-u[n][j]))
#			uleft=(1/2.*(u[n][j]+u[n][j-1])-v*dt/(2.*dx)*(u[n][j]-u[n][j-1]))
			u[n+1].append(u[n][j]-dt/dx*(Fup_-Fdo_))
#			u[n+1].append(u[n][j]-v*dt/dx*(uright-uleft))
			j+=1
		u[n].pop()	
		u[n].pop()	
		u[n].pop(0)	
		u[n].pop(0)	
		u[n+1].append(1.)	#upper boundary
		print len(u[n])
#		u[n+1].append(u[n+1][NX-2]+3*u[n+1][NX-3]+u[n+1][NX-4])
		n+=1
	return u


def startcond(NX,NT,dx,dt):
	u=[[]]
	j=0
	n=0
	while j<NX:
		u[0].append(2./np.cosh(j*dx))	# index 0 is time, 1 is position
		j+=1
	return u


	
def main():
	T=1.	#timeinterval
	X=10.	#spaceinterval
	NX=500
	dx=X/float(NX)
	dt=0.005
	NT=int(T/dt)
	v=1.
	j=0
	n=0
	uwen=LAX_WENDROF_con(NX,NT,dx,dt,v)
	print uwen[NT-1]
#	taxe=np.linspace(0,T,len(u))
#	plt.plot(xaxe,u[0],color='b')
#	plt.plot(xaxe,function(0.05,xaxe),color='y')
	xaxe=np.linspace(0,X,NX)
	plt.plot(xaxe,uwen[NT-1])
	plt.plot(xaxe,uwen[0])
	plt.show()
if __name__=="__main__":
	main()
