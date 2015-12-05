#/usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def makeB(NX,NY):
	B=np.diag(np.linspace(1,1,NX*NY),0)+np.diag(np.linspace(-1,-1,NX*NY-1),1)+np.diag(np.linspace(-1,-1,NX*NY-1),-1)+np.diag(np.linspace(-1,-1,NX*NY-NX),NX)+np.diag(np.linspace(-1,-1,NX*NY-NX),-NX)
	return B		

def transform(NX,NY,u):
	ut=[[]]
	x=0
	y=0
	while x<NX:
		while y<NY:
			ut[x].append(u[x+y*NX])
			y+=1
		ut.append([])
		x+=1
	return ut

def initu(NX,NY,dx,dy):
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

def iter(B,u):
	u_=np.dot(B,u)
	return u_

def main(argv):
	X=2.
	Y=2.
	NX=100
	NY=100
	dx=X/NX
	dy=Y/NY
	B=makeB(NX,NY)
	u=initu(NX,NY,dx,dy)
	print len(u)
	itnum=10	
	i=0
	while i<itnum:
		u=iter(B,u)
		i+=1
	print len(u)
	ut=transform(NX,NY,u)
#	plt.plot2d(np.linspace(-1,1,NX*NY),ut[:][0])
	xs=np.linspace(-1,1,NX)
	ys=np.linspace(-1,1,NY)

	Axes3D.plot(xs,ys,ut)
#	plt.show()


if __name__=="__main__":
	main(sys.argv)
