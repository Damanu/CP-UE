#/usr/bin/python!

import sys
import numpy as np


def makeA():
	i=1
	j=1
	k=1
	l=1
	A=np.zeros((8,8,8,8))
	while i<=8:
		j=1
		while j<=8:
			k=1
			while k<=8:
				l=1
				while l<=8:
					if i==k and j==l:
						A[i-1][j-1][k-1][l-1]=-4.
					elif (i==k and j==l+1) or (i==k+1 and j==l) or (i==k and j==l-1) or (i==k-1 and j==l):
						A[i-1][j-1][k-1][l-1]=1.
					else:
						A[i-1][j-1][k-1][l-1]=0.
						
					l+=1
				k+=1
			j+=1
		i+=1

	return A

def makeP():
	i=1	#bis 8
	j=1	#bis 8
	k=1	#bis 4
	l=1	#bis 4
	P=np.zeros((8,8,4,4))
	while i<=8:
		j=1
		while j<=8:
			k=1
			while k<=4:
				l=1
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
	R=np.zeros((4,4,8,8))
	i=0
	j=0
	k=0
	l=0
	c=1/4.
	while i<8:
		j=0
		while j<8:
			k=0
			while k<4:
				l=0
				while l<4:
					R[k][l][i][j]=c*P[i][j][k][l]
					l+=1
				k+=1
			j+=1
		i+=1
	return R

def RAP(R,A,P):
	i=0
	j=0
	k=0
	l=0
	m=0
	n=0
	m_=0
	n_=0
	U=np.zeros((8,8,4,4))
	A_=np.zeros((4,4,4,4))
	while i<4:
		j=0
		while j<4:
			k=0
			while k<4:
				l=0
				while l<4:
					m=0
					while m<8:
						n=0
						while n<8:
							m_=0
							while m_<8:
								n_=0
								while n_<8:
									U[m][n][k][l]+=A[m][n][m_][n_]*P[m_][n_][k][l]
									n_+=1
								m_+=1
							print("i=",i," j=",j," k=",k," l=",l," m=",m," n=",n)
							A_[i][j][k][l]+=R[i][j][m][n]*U[m][n][k][l]
							n+=1
						m+=1
					l+=1
				k+=1
			j+=1
		i+=1
	return A_

def main():
	A=makeA()
#	print "A\n",A
	P=makeP()
#	print "\nP\n",P
	R=makeR(P)
	A_=RAP(R,A,P)
	i=1
	j=1
	k=1
	l=1
#	Ah[i,j,k,l]=sum(sum(R[i][j][:][:]*sum(sum(A[m][n][:][:]*P[:][:][k][l]))))
#	Ah=np.dot(R,np.dot(A,P))
#	print "\nR\n",R
#	print "\nR*A*P\n",RAP(R,A,P)
	print A[0]
	print A_[0]
#	print Ah[1][1]
if __name__=="__main__":
	main()
