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
	print "N"
	print N
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
	
def IFT(data):
	N=len(data)
	print "N"
	print N
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
	print "N"
	print N
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
	fi_plot=[]
	fn_plot=[]
	filong_plot=[]
	fi=Read()
	fi=map(complex,fi)
	print len(fi)	
#	fi[:]=np.linspace(0,1,100)
	N=len(fi)
	i=0
	for x in fi:
		fi_plot.append(0)
		fi_plot[i]=x.real
		i+=1
	print len(fi_plot)
	plotfi1=plt.subplot(4,1,1)
	plotfi1=plt.plot(np.linspace(0,1,N),fi_plot[:])
	plotfi1=plt.title("fi")
#	print "fi", fi
	fn=FT(fi)
	i=0
	for x in fn:
		fn_plot.append(0)
		fn_plot[i]=x.real
		i+=1
	plotfn=plt.subplot(4,1,2)
	plotfn=plt.plot(np.linspace(0,1,N),fn_plot[:])
	plotfn=plt.title("fn")
	Write(fn)
#	print "fn",fn
	fi=IFT(fn)
	filong=IFTlong(fn)
	i=0
	for x in fi:
		fi_plot.append(0)
		fi_plot[i]=x.real
		i+=1
	i=0
	for x in filong:
		filong_plot.append(0)
		filong_plot[i]=x.real
		i+=1
#	print "fi",fi
	plotfi=plt.subplot(4,1,3)
	plotfi=plt.plot(np.linspace(0,1,N),fi_plot[0:N])
	plt.title("fi")
	plotfilong=plt.subplot(4,1,4)
	plotfilong=plt.plot(np.linspace(0,2,2*N),filong_plot)
	plt.title("fi-long")
#	fn=FT(fi)
#	plotfn2=plt.plot(np.linspace(0,1,N),fn)
#	plotfn2=plt.subplot(4,1,4)
	plt.show()
if __name__=="__main__":
	main()
