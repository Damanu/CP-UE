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
	i=1	#bis 8
	j=1	#bis 8
	k=1	#bis 4
	l=1	#bis 4
	P=np.zeros((8,8,4,4))
	P=np.concatenate((P,P))
	print P
	while i<=8:
		j=0
		while j<=8:
			k=0
			while k<=4:
				l=0
				while l<=4:
					if i==2*k and j==2*l:
						P[i-1][j-1][k-1][l-1]=1
					elif (i==2*k and j==2*l+1) or (i==2*k+1 and j==2*l) or (i==2*k and j==2*l-1) or (i==2*k-1 and j==2*l):
						P[i-1][j-1][k-1][l-1]=1/2.
					elif (i==2*k+1 and j==2*l+1) or (i==2*k+1 and j==2*l-1) or (i==2*k-1 and j==2*l-1) or (i==2*k-1 and j==2*l+1):
						P[i-1][j-1][k-1][l-1]=1/4.
					else:
						P[i-1][j-1][k-1][l-1]=0.
						
					l+=1
				k+=1
			j+=1
		i+=1
	return P
	
		
def makeR(P):
	R=np.zeros((8,8,4,4))
	i=0
	j=0
	k=0
	l=0
	while i<8:
		j=0
		while j<8:
			k=0
			while k<4:
				l=0
				while l<4:
					R[i][j][l][k]=1/4.*P[i][j][k][l]
					l+=1
				k+=1
			j+=1
		i+=1
	return R
def main():
#	A=makeA()
#	print "A\n",A
	P=makeP()
#	print "\nP\n",P
	R=makeR(P)
	print "\nR\n",R
	print "\nR*A*P\n",R*A*P


if __name__=="__main__":
	main()
