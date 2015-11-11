#usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt 
import time
import random
import scipy.fftpack as sfft

PATH="./"
OUTFILE="FT_data.txt"
INFILE="Compl_num.txt"
#----------subroutines--------------
def Read():
	data=[]		#data equals my fouriercoeffitients fi
	try:
		text = open(PATH+INFILE,'r')	#open file to read
		data=text.read().splitlines()
		text.close()
		return data		
	except:
		print 'Something went wrong at %argv[0] subprogram Read() while reading the datafile'
		sys.exit()
def Write(data):
	text = open(PATH+OUTFILE,'w+')	#open filen to write
	for x in data:
		text.write(str(x)+"\n")	#write data to file 
	text.close()

def FT(data):
	N=len(data)
#	print "N"
#	print N
	fn=[]
	map(complex,data)
	map(complex,fn)
	n=0
	while n<N:
		i=0
#		print "n=",n+N/2
		fn.append(0.0j)
		for fi in data:
			fn[n]+=1.0/(N)*np.exp(-(2.0*np.pi*n*1.0j*i)/(N))*fi
#			prinnt i
			i+=1
		n+=1
	return fn

def FTlong(data):
	N=len(data)
#	print "N"
#	print N
	fn=[]
	map(complex,data)
	map(complex,fn)
	n=-N/2
	i=-N/2
	while n<=N/2-1+N:
#		print "n=",n+N/2
		fn.append(0.0j)
		for fi in data:
			fn[n+N/2]+=1.0/(N)*np.exp(-2.0*np.pi*n*1.0j*i/(N))*fi
#			print i
			i+=1
		n+=1
		i=-N/2
	return fn
	
def IFT(data):
	N=len(data)
#	print "N"
#	print N
	fn=[]
	map(complex,data)
	map(complex,fn)
	n=0
	while n<N:
		i=0
#		print "n=",n+N/2
		fn.append(0.0j)
		for fi in data:
			fn[n]+=np.exp((2.0*np.pi*n*1.0j*i)/(N))*fi
#			prinnt i
			i+=1
		n+=1
	return fn



def IFTlong(data):
	N=len(data)
#	print "N"
#	print N
	fn=[]
	map(complex,fn)
	n=-N/2
	i=-N/2
	while n<=(N/2-1+N):
#		print "n=",n+N/2
		fn.append(0.0)
		for fi in data:
			fn[n+N/2]+=1.0*np.exp(2.0*np.pi*n*1.0j*i/N)*fi
#			print i
			i+=1
		n+=1
		i=-N/2
	return fn


#--------------Main Program---------------
def main():
	fi=[]
	N=64
	L=0.1
	sig=0.01
	mu=0.
	i=-N/2
	while i <=N/2-1:
		x=i*L/N
		fi.append(random.randrange(-3,3)+1./(sig*np.sqrt(2*np.pi))*np.exp(-1/2.*((x-mu)/sig)**2))
		i+=1
		print x

	fn=sfft.fft(fi)
	x=np.linspace(-N/2,N/2-1,N)*L/N
#	fn=sfft.fft(random.randrange(-3,3)+1./(sig*np.sqrt(2*np.pi))*np.exp(-1/2.*((x-mu)/sig)**2))
#----------Filter--------------
#	i=0
#	for x in fn:
#		if i>20 and i<40:
#			fn[i]=0	
#		i+=1
#----------------------
	x=np.linspace(-L,L,N)
	fit=sfft.ifft(fn)
	plt.subplot(3,2,1)
	plot2=plt.plot(x,fi)
	plt.subplot(3,2,3)
	plot1=plt.plot(x,fn)
	plt.subplot(3,2,5)
	plot3=plt.plot(x,fit)
#	plt.show()

#----------------------------------------------------
	fn=FT(fi)
	
#----------Filter--------------
	i=0
	for x in fn:
		if i>20 and i<40:
			fn[i]=0	
		i+=1
#----------------------
	x=np.linspace(-L,L,N)
	fit=IFT(fn)
	plt.subplot(3,2,2)
	plot2=plt.plot(x,fi)
	plt.subplot(3,2,4)
	plot1=plt.plot(x,fn)
	plt.subplot(3,2,6)
	plot3=plt.plot(x,fit)
	plt.show()
if __name__=="__main__":
	main()
