#/usr/bin/python!

import matplotlib.pyplot as plt
import numpy as np
import sys


def rgen(i0,a,c,m,length):
	i=[i0]
	ch=[i0/m]
	j=1
	while j<length:
		i.append((a*i[j-1]+c)%m)
		ch.append(i[j]/m)
		j+=1
	return [i,ch]

def main():
	i0=1.
	c=1.
	m=256
	a=55
#	while a<=60:
	(i,ch)=rgen(i0,a,c,m,256)
	x=np.linspace(0,19,256)
	plt.plot(x,i)
	plt.show()	

if __name__=="__main__":
	main()
