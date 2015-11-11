#usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt 

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
	N=220
	T=5.
	dt=T/N
	print "dt",dt
	omg=2.*np.pi/dt
	print "omg",omg
	i=0
	ti=0
	while i<=N-1:
		ti+=dt
		if i<0:
			fi.append(0j)
		else:
			fi.append(np.exp(-ti)+0.j)	
		i+=1
	fn=FT(fi)
	fnlong=FTlong(fi)
	fn_fft=np.fft.ifft(fi)
	fit=IFT(fn)
	x1=np.linspace(-omg/2.,omg/2.,N)
	x2=np.linspace(0,T,N)
	x3=np.linspace(-omg/2,omg/2+omg,2*N)
	i=0
	for x in fn:
		fn[i]=x.real
		i+=1

	plt.subplot(3,1,1)
	plot2=plt.plot(x2,fi)
	plt.subplot(3,1,2)
	plot1=plt.plot(x2,fit)
	plt.subplot(3,1,3)
	plot3=plt.plot(x1,fn)
	plt.show()
if __name__=="__main__":
	main()
