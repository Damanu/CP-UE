#/usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm

def makeA(NX,NY):
	A=np.diag(np.ones(NX*NY),0)-np.diag(np.ones(NX*NY-1),1)/4-np.diag(np.ones(NX*NY-1),-1)/4-np.diag(np.ones(NX*NY-NX),NX)/4-np.diag(np.ones(NX*NY-NX),-NX)/4
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
	NY=len(u[0])
	x=0
	while x<NX:
		y=0
		while y<NY:
			u_.append(u[x][y])
			y+=1
		x+=1
	return u_
	
def initu(NX,NY,dx,dy): 	#randbedignung der dgl
	u=np.linspace(0,0,NX*NY)
	i=0
	while i<NX:
		u[i]=1.
		u[-i]=1.
		i+=1
	i=0
	while i<NY:
		u[i*NX]=1.
		u[i*NX+NX-1]=1.
		i+=1
	return u	

def iter(B,roh,u):
	u_=np.dot(B,u)+roh
	return u_

def mkroh(NX,NY):	#ladungsdichte
	roh=[]
	x=0
	y=0
	while x<NX:
		y=0
		roh.append([])
		while y<NY:
	#		if y<3*NY/4 and y>NY/4 and x==3*NX/4:
	#			roh[x].append(-10.)
	#		elif y<3*NY/4 and y>NY/4 and x==3*NX/4+2:
	#			roh[x].append(10.)
	#		elif y<3*NY/4 and y>NY/4 and x==NX/4:
	#			roh[x].append(10.)
	#		elif y<3*NY/4 and y>NY/4 and x==NX/4-2:
	#			roh[x].append(-10.)
#			if y==3*NY/4 and x==NX/2:
#				roh[x].append(10.)
#			elif y==NY/4 and x==NX/2:
#				roh[x].append(-10.)
			if y<NY/2 and y>NY/4 and x==NX/2:
				roh[x].append(-10.)
			elif y>=NY/2 and y<3*NY/4 and x==NX/2:
				roh[x].append(10.)
			else:
				roh[x].append(0.)
			y+=1
		x+=1
	print roh
	roh=transform_(roh)
	print roh
	return roh


def main(argv):
	X=1.
	Y=1.
	NX=40
	NY=40

	dx=X/NX
	dy=Y/NY
	A=makeA(NX,NY)
	B=makeB(NX,NY,A)
	roh=mkroh(NX,NY)
	u=initu(NX,NY,dx,dy)
	itnum=10	
	i=0
	eps=1
	while eps>0.001:
		print i
		u_=iter(B,roh,u)
		eps=max(u-u_)
		print eps
		u=u_
		i+=1


	ut=transform(NX,NY,u)
	uy,ux=np.gradient(ut)
	x=np.linspace(0,X,NX)
	y=np.linspace(0,Y,NY)
	fig,ax=plt.subplots()
	im = ax.imshow(ut, extent=[0, X, 0, Y])
	ax.quiver(x,y,-ux,-uy)
	fig.colorbar(im)
	ax.set(aspect=1,title="Electric field")
	plt.show()
	
#	plt.plot2d(np.linspace(-1,1,NX*NY),ut[:][0])
#	xs=np.linspace(-1,1,NX)
#	ys=np.linspace(-1,1,NY)

#	Axes3D.plot(xs,ys,ut)
##	plt.show()


if __name__=="__main__":
	main(sys.argv)
