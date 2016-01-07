#/usr/bin/python!

import sys
import numpy as np


def makeA():
	i=1
	a=[[-2,1,0,0,0,0,0,1]]
	A=np.matrix(a)
	print len(a[0])
	while i<8:
		A=np.concatenate((A,np.roll(a,i)))
		i+=1
	return A

def makeP():
	i=1
	a=[[1,0,0,0]]
	b=[[1/2.,1/2.,0,0]]
	P=np.matrix(a)
	P=np.concatenate((P,b))
	while i<4:
		P=np.concatenate((P,np.roll(a,i)))
		P=np.concatenate((P,np.roll(b,i)))
		i+=1
	return P
		
def makeR(P):
	R=P.T*1/2.
	return R
def main():
	A=makeA()
	print "A\n",A
	P=makeP()
	print "\nP\n",P
	R=makeR(P)
	print "\nR\n",R
	print "\nR*A*P\n",R*A*P


if __name__=="__main__":
	main()
