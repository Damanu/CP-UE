#/usr/bin/python!

import sys
import numpy as np


def makeA():
	N=8
	i=0
	j=0
	k=0
	l=0
	A=np.zeros((N,N,N,N))
	while i<N:
		j=0
		while j<N:
			k=0
			while k<N:
				l=0
				while l<N:
					if i==k and j==l:
						A[(i)][(j)][(k)][(l)]=-4.
					elif (i==k and j==(l+1)%N) or (i==(k+1)%N and j==l) or (i==k and j==(l-1)%N) or (i==(k-1)%N and j==l):
						A[(i)][(j)][(k)][(l)]=1.
					else:
						A[(i)][(j)][(k)][(l)]=0.
						
					l=l+1
				k+=1
			j+=1
		i+=1

	return A

def makeP():
	N=8
	i=0	#bis 7
	j=0	#bis 7
	k=0	#bis 3
	l=0	#bis 3
	P=np.zeros((N,N,N/2,N/2))
	while i<N:
		j=0
		while j<N:
			k=0
			while k<N/2:
				l=0
				while l<N/2:
					if i==2*k and j==2*l:
						P[i][j][k][l]=1.
					elif (i==2*k and j==(2*l+1)%N) or (i==(2*k+1)%N and j==2*l) or (i==2*k and j==(2*l-1)%N) or (i==(2*k-1)%N and j==2*l):
						P[i][j][k][l]=1/2.
					elif (i==(2*k+1)%N and j==(2*l+1)%N) or (i==(2*k+1)%N and j==(2*l-1)%N) or (i==(2*k-1)%N and j==(2*l-1)%N) or (i==(2*k-1)%N and j==(2*l+1)%N):
						P[i][j][k][l]=1/4.
					else:
						P[i][j][k][l]=0.
						
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
	c=1/2.
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

def RAP_easy(R,A,P):
	N=8
	m=0	#bis 7 u 3
	n=0	#bis 7 u 3	
	k=0	#bis 3
	l=0	#bis 3
	i=0	#bis 3
	j=0	#bis 3

	U=np.zeros((N,N,N/2,N/2))	
	A2h=np.zeros((N,N,N/2,N/2))	

	while m<N:
		n=0
		while n<N:
			k=0
			while k<N/2:
				l=0
				while l<N/2:
					U[m,n,k,l]=sum(sum(A[m,n,:,:]*P[:,:,k,l]))
					l+=1
				k+=1
			n+=1
		m+=1
	i=0
	while i<N/2:
		j=0
		while j<N/2:
			k=0
			while k<N/2:
				l=0
				while l<N/2:
					A2h[i,j,k,l]=sum(sum(R[i,j,:,:]*U[:,:,k,l]))
					l+=1
				k+=1
			j+=1
		i+=1
	return A2h

def main():
	A=makeA()
#	print "A\n",A
	P=makeP()
	R=makeR(P)
	A2h=RAP_easy(R,A,P)
	i=1
	j=1
	k=1
	l=1
	
#	Ah[i,j,k,l]=sum(sum(R[i][j][:][:]*sum(sum(A[m][n][:][:]*P[:][:][k][l]))))
#	Ah=np.dot(R,np.dot(A,P))
#	print "\nR\n",R
#	print "\nR*A*P\n",RAP(R,A,P)
#	print "\nP\n",P[:][0][:]
#	print A
	print A2h[0][0]
#	print Ah[1][1]
if __name__=="__main__":
	main()
