#usr/bin/python!

import sys
import numpy as np
import matplotlib.pyplot as plt 

PATH="./"
FILE="Compl_num.txt"

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
	text = open(PATH+FILE,'w+')	#open filen to write
	for x in data:
		text.write(str(x)+"\n")	#write data to file 
	text.close()



#--------------Main Program---------------
def main():

	fi=[]
	i=0
	N=300
	while i<N:
		fi.append(0j)
		if i>=N/2-2*N/100 and i<=N/2+2*N/100:
			fi[i]=1+0j
		else:
			fi[i]=0j
		i+=1
	Write(fi)
if __name__=="__main__":
	main()
