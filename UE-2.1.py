#/usr/bin/python!

import numpy as np
import matplotlib.pyplot as plt
import sys

def fweu(func,dx):
	N=len(func)
	fx=[]
	i=0
	while i<N-1:
		fx.append((func[i+1]-func[i])/dx)
		i+=1
	return fx		

def fbeu(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N:
		fx.append((func[i]-func[i-1])/dx)
		i+=1
	return fx		

def fzd(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N-1:
		fx.append((func[i+1]-func[i-1])/(2*dx))
		i+=1
	return fx		

def fzd2(func,dx):	#functions starts at second point (so fx[0]=fx_real[1])
	N=len(func)
	fx=[]
	i=1
	while i<N-1:
		fx.append((func[i+1]-2*func[i]+func[i-1])/(dx**2))
		i+=1
	return fx		




def sd(func,func_real):	#standard deviation
	N=len(func)
	var=0	
	i=0
	while i < N:
		var+=(func[i]-func_real[i])**2
		i+=1
	return np.sqrt(var/N*1.)

def main():
	sfw=[]
	sbw=[]
	szd=[]
	szd2=[]
	M=50	#max number of steps
	dN=1	#stepsize
	N=3	#startingpoint
	while N<=M:
		N_real=N
		L=1.
		dx=L/N
		x=np.linspace(0,1,N)
		x_real=np.linspace(0,1,N_real)

		y=np.sin(np.pi*x)	#defining function
		y_real=np.sin(np.pi*x_real)	
		yx_real=np.cos(np.pi*x_real)*np.pi
		yxx_real=-np.sin(np.pi*x_real)*np.pi**2


	#---------derivations------------------
		yxfw=fweu(y,dx)		#deriving with forward euler
		yxbw=fbeu(y,dx)		#deriving with backward euler
		yxzd=fzd(y,dx)		#deriving with zentral difference
		yxxzd=fzd2(y,dx)	#deriving with 2nd zentral diff

	#------	standard deviations---------------------------------------------
		sfw.append(sd(yxfw,yx_real))
		sbw.append(sd(yxbw,yx_real[1:]))
		szd.append(sd(yxzd,yx_real[1:-1]))
		szd2.append(sd(yxxzd,yxx_real[1:-1]))

		N+=dN
		
		
#	plt.plot(x[0:N-1],yxfw_err)	
#	plt.plot(x[1:len(yxzd)+1],yxzd)
#	plt.plot(x_real,y_real)
#	plt.plot(x_real,yx_real)
	xaxe=np.linspace(1./3,dx,M/dN-2)
	plt.subplot(4,1,1)
	plt.title("fw")
	plt.plot(xaxe,np.log(sfw))
	plt.subplot(4,1,2)
	plt.title("bw")
	plt.plot(xaxe,np.log(sbw))
	plt.subplot(4,1,3)
	plt.title("zd")
	plt.plot(xaxe[1:N],np.log(szd[1:N]))
	plt.subplot(4,1,4)
	plt.title("bw2")
	plt.plot(xaxe,np.log(szd2))
	plt.show()

if __name__=="__main__":
	main()
