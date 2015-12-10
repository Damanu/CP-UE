#/usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt

def roh(xaxe):
	roh=[]
	for x in xaxe:
		if x>-1/2. and x<0:
			roh.append(-1.)
		elif x>0 and x<1/2.:
			roh.append(1.)
		else:
			roh.append(0.)	
	return roh



def func(roh,dx):
	func=[]
	for x in roh:
		func.append(-x*2.*dx**2)
	return func

def func2(roh,dx):
	func=[]
	for x in roh:
		func.append(-x*2.)
	return func


def alpha(a,b,c,alph,NX):
	i=0
	while i<NX:
		alph.append(-a/(b+alph[-1]*c))
		i+=1
	return alph	

def beta(b,c,y,alph,bet,NX):
	i=0
	while i<NX:
		bet.append((y[i]-bet[i]*c)/(b+alph[i]*c))
		i+=1
	return bet
def getx(alph,bet,x,NX):
	i=NX
	while i>0:
		x[i-1]=alph[i]*x[i]+bet[i]
		i-=1
	return x

def thomas(X,dx,NX):
	a=1
	b=-2
	c=1
	alph=[0.]
	bet=[0.]
	x=np.linspace(0,0,NX+1)
	xaxe=np.linspace(X[0],X[1],NX)
	
	y=func(roh(xaxe),dx)

	alph=alpha(a,b,c,alph,NX)
	bet=beta(b,c,y,alph,bet,NX)

	x=getx(alph,bet,x,NX)

	plt.title("Thomas-algorithm")
	plt.plot(xaxe,roh(xaxe))
	plt.plot(xaxe,x[0:NX])
	plt.show()
	
#-------------------------------------------------
def costraf(u,N):
	NX=len(u)
	u_=[]
	j=np.linspace(0,NX-1,NX) #summation index from 1. element to last. 
	n=0
	while n<NX:
#		cosum=sum(np.cos(n*np.pi*j/NX)[1:NX]*u[1:NX])
		j=1
		cosum=0
		while j<NX:
			cosum+=(np.cos(n*np.pi*j/N)*u[j])
			j+=1
		u_.append(1./2.*(u[0]+(-1.)**(1.*n)*u[NX-1])+2.*cosum/N)
		n+=1
	return u_

def Icostraf(u,N):
	NX=len(u)
	print NX
	u_=[]
	j=np.linspace(0,NX-1,NX)
	n=0
	while n<NX:
	#	cosum=sum(np.cos(n*np.pi*j/NX)[1:NX]*u[1:NX])
		j=1
		cosum=0
		while j<NX:
			cosum+=(np.cos(n*np.pi*j/N)*u[j])
			j+=1
		u_.append(1./2.*(u[0]+(-1.)**(1.*n)*u[NX-1])+cosum)
		n+=1
	return u_
	

def solve_traf(roh_,dx):
	NK=len(roh_)
	j=np.linspace(0,NK-1,NK)
	print j
	phi_=dx**2*np.array(roh_)[1:NK]/(2.*np.cos(j*np.pi/NK)[1:NK]-2.)
	return phi_

def fanalys(X,dx,NX):	
	xaxe=np.linspace(X[0],X[1],NX)
	r=func2(roh(xaxe),dx)
	print len(r)
	r_=costraf(r,NX)
	phi_=solve_traf(r_,dx)
	phi_=np.insert(phi_,0,0.)
	phi=Icostraf(phi_,NX)
	print phi
	plt.title("F-analysis")
#	plt.plot(xaxe,roh(xaxe))
	plt.plot(xaxe,(phi)[0:NX])
#	plt.plot(xaxe,phi_[0:NX])
#	plt.plot(xaxe,(costraf(np.cos(xaxe))))
	plt.show()
#---------------------------------------------------
def main(argv):
	mode=argv[1]	

	X=[-1.,1.]
	dx=0.02
	NX=int((X[1]-X[0])/dx)

	if mode=="a":
		thomas(X,dx,NX)
	if mode=="b":
		fanalys(X,dx,NX)

if __name__=="__main__":
	main(sys.argv)
