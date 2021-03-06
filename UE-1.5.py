#usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt 

PATH="./"
FILE="data"

#----------subroutines--------------
def Read():
	data=[]		#data equals my fouriercoeffitients fi
	try:
		text = open(PATH+FILE,'r')	#open file to read
		data=text.read().splitlines()
		text.close()
		return data		
	except:
		print 'Something went wrong at %argv[0] subprogram Read() while reading the datafile'
		sys.exit()
def Write(data):
	text = open(PATH+"FT_data",'w+')	#open filen to write
	for x in data:
		text.write(str(x)+"\n")	#write data to file 
	text.close()

def FT(data):
	N=len(data)
	print "N"
	print N
	fn=[]
	map(complex,fn)
	n=-N/2
	i=-N/2
	while n<=N/2-1:
#		print "n=",n+N/2
		fn.append(0.0j)
		for fi in data:
			fn[n+N/2]+=1.0*complex(np.exp(-2.0*np.pi*n*1.0j*i/(N)))*fi
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
		fn.append(0.j)
		for fi in data:
			fn[n+N/2]+=1.0*np.exp(2.0*np.pi*n*1.0j*i/(1.*N))*fi
#			print i
			i+=1
		n+=1
		i=-N/2
	return fn


#--------------Main Program---------------
def main():
#	fi=Read()
#	fi[:]=np.linspace(0,1,100)
	N=100
	fi=[]
	n=-N/2
	while n<=N/2-1:
		fi.append(0.j)
		if n==0:
			fi[n+N/2]=1./3. + 0.0j
		elif n!=0:
			fi[n+N/2]=3.0/((n*np.pi)**2)*(np.sin(n*np.pi/3.0))**2.	
		n+=1
#	N=len(fi)
#	fi=map(complex,fi)
	i=0
	for x in fi:
		fi[i]=x.real
	plotfi1=plt.plot(np.linspace(-3/2.,3./2,N),fi[0:N])
	print "fi", fi
	fn=IFT(fi)



#	Write(fn)
#	print "fn",fn
#	fi=FT(fn)
#	print "fi",fi
	plotfn=plt.plot(np.linspace(-3./2,3./2,N),fn)
#	plotfi=plt.plot(np.linspace(0,1,N),fi)
#	fn=FT(fi)
#	plotfn2=plt.plot(np.linspace(0,1,N),fn)
	plt.show()
if __name__=="__main__":
	main()
