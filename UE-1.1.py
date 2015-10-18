#usr/bin/python!

import sys
import numpy as np

PATH="./"
FILE="data"

#----------subroutines--------------
def Read():
	data=[]		#data equals my fouriercoeffitients fi
	try:
		text = open(PATH+FILE,'r')	#open file to read
		data.append(text.readline())
		return data		
	except:
		print 'Something went wrong at %argv[0] subprogram Read() while reading the datafile'
		sys.exit()
def FT(data):
	N=len(data)
	fn=[]
	n=-N/2
	i=0
	for fi in data:
		fn[n+N/2]=(1/N*np.exp(-2*np.pi*n*1j*i/N)*data)
		n+=1
	
		fn.append(0)
	

