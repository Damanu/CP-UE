#/usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def makeA(NX,NY):
	A=-np.diag(np.ones(NX*NY),0)*4+np.diag(np.ones(NX*NY-1),1)+np.diag(np.ones(NX*NY-1),-1)+np.diag(np.ones(NX*NY-NX),NX)+np.diag(np.ones(NX*NY-NX),-NX)
	return A

def makeB(NX,NY,A):
	B=np.diag(np.ones(NX*NY),0)-A	
	return B

def transform(NX,NY,u):
	ut=[]
	x=0
	y=0
	while x<NX:
		y=0
		ut.append([])
		while y<NY:
			ut[x].append(u[x+y*NX])
			y+=1
		x+=1
	return ut

def transform_(u):
	u_=[]
	NX=len(u)
	x=0
	while x<NX:
		u_.append(u[x])
		x+=1

def initu(NX,NY,dx,dy): 	#randbedignung der dgl
	u=np.linspace(0,0,NX*NY)
	i=0
	while i<NX:
		u[i]=(dx*i-NX*dx/2.)**2.-1.
		u[-i]=(dx*(NX-i-1)-NX*dx/2.)**2.-1.
		i+=1
	i=0
	while i<NY:
		u[i*NX]=1.-(dy*i-NY*dy/2.)**2.
		u[i*NX+NX-1]=1.-(dy*i-NY*dy/2.)**2.
		i+=1
	return u	

def iter(B,roh,u):
	u_=np.dot(B,u)+roh
	return u_

def mkroh(NX,NY):	#ladungsdichte
	roh=np.zeros(NX*NY)
	return roh


def main(argv):
	X=2.
	Y=2.
	NX=100
	NY=100
	dx=X/NX
	dy=Y/NY
	A=makeA(NX,NY)
	B=makeB(NX,NY,A)
	roh=mkroh(NX,NY)
	u=initu(NX,NY,dx,dy)
	itnum=10	
	i=0
	eps=1
	while eps>0.01:
		print i
		u_=iter(B,roh,u)
		eps=abs(np.mean(u)-np.mean(u_))
		u=u_
		i+=1


	ut=transform(NX,NY,u)
	ux,uy=np.gradient(ut)
	x=np.linspace(0,X,NX)
	y=np.linspace(0,Y,NY)
	fig,ax=plt.subplots()
	ax.quiver(x,y,ux,uy,ut)
	ax.set(aspect=1,title="bla")
	plt.show()
	
#	plt.plot2d(np.linspace(-1,1,NX*NY),ut[:][0])
#	xs=np.linspace(-1,1,NX)
#	ys=np.linspace(-1,1,NY)

#	Axes3D.plot(xs,ys,ut)
##	plt.show()


if __name__=="__main__":
	main(sys.argv)
