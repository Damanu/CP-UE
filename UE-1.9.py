#usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt 
import time

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
	n=-N/2
	i=-N/2
	while n<=N/2-1:
#		print "n=",n+N/2
		fn.append(0.0j)
		for fi in data:
			fn[n+N/2]+=1.0/(N)*np.exp(-2.0*np.pi*n*1.0j*i/(N))*fi
#			print i
			i+=1
		n+=1
		i=-N/2
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
	map(complex,fn)
	n=-N/2
	i=-N/2
	while n<=(N/2-1):
#		print "n=",n+N/2
		fn.append(0.0)
		for fi in data:
			fn[n+N/2]+=1.0*np.exp(2.0*np.pi*n*1.0j*i/N)*fi
#			print i
			i+=1
		n+=1
		i=-N/2
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
	tft=[]
	tfft=[]
	Nmax=60
	N=2
	while N<=Nmax:
		i=0
		while i<N:
			fi.append(np.cos(i*2*np.pi/N)+0.j)
			i+=1
		N+=2	
		start=time.time()
		FT(fi)
		end=time.time()
		tft.append(end-start)
		start=time.time()
		np.fft.fft(fi)
		end=time.time()
		tfft.append(end-start)

	x=np.linspace(2,Nmax,Nmax/2)
	plt.subplot(2,1,1)
	plot2=plt.plot(x,tft)
	plt.subplot(2,1,2)
	plot1=plt.plot(x,tfft)
#	plt.subplot(3,1,3)
#	plot3=plt.plot(x1,fn)
	plt.show()
if __name__=="__main__":
	main()
