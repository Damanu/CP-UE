#/usr/bin/python!

<<<<<<< HEAD
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
	
def fourier(X,dx,NX):
	


def main(argv):
	mode=argv[1]	

	X=[-1.,1.]
	dx=0.02
	NX=int((X[1]-X[0])/dx)

	if mode=="a":
		thomas(X,dx,NX)
	if mode=="b":
		


if __name__=="__main__":
=======




def main(argv):
	

if __name__="__main__":
>>>>>>> aece44baf60133cec1ee6f54f87114ba55e28777
	main(sys.argv)
