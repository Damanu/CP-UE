#/usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt

def makeB(NX):
	i=0
	j=0
	B=[]
	while i<NX:
		im1=(i-1+NX)%NX
		im2=(i-2+NX)%NX
		ip1=(i+1)%NX
		ip2=(i+2)%NX
		ip3=(i+3)%NX
		B.append(list(np.linspace(0.,0.,NX)))
		B[i][im1]=1./2.
		B[i][ip1]=1./2.
		i+=1
		if i<NX:
			B.append(list(np.linspace(0.,0.,NX)))
			B[i][im2]=1./4
			B[i][i]=1./2
			B[i][ip2]=1./4
			i+=1	
	return B

def BmI(B):
	NX=len(B[0])
	i=0

	while i<NX:
		B[i][i]-=1
		i+=1	
	return B


def folge(A,x):
	NX=len(x)
	i=0
	j=0
#	print"x", x[-1]
	#print "A",A
	x.append(list(np.dot(A,x[-1])/np.linalg.norm(x[-1])))	
	return x

def getev(x):
	ev=np.dot(x[-1],x[-2])
	return ev

def normgs(NX):
	X=1.
	dx=X/NX
	x=[]
	x=[list(np.linspace(1.,-1.,NX))]
	itnum=20
	A=makeB(NX)
	i=0
	while i<itnum:
		x=folge(A,x)
		i+=1
	lam=getev(x)
	return lam
	
	



def main(argv):
	NX=2
	lam=[]
	lamj=[]
	lamgs=[]
	NXmax=200
	while NX<NXmax:
		lam.append((normgs(NX)))
		print lam[-1]
		lamj.append((1-2*np.pi/NX**2))
		lamgs.append((1-4*np.pi/NX**2))
		NX+=2
	xaxe=np.linspace(2,NXmax,len(lam))
	plt.plot(xaxe,lam)
	plt.plot(xaxe,lamj)
	plt.plot(xaxe,lamgs)
	plt.show()

if __name__=="__main__":
	main(sys.argv)











