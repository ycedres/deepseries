#!/usr/bin/python

import numpy as np
from scipy.io import savemat
import datetime

numlineas = 0
with open('torreME_editado.txt','r') as f:
    for line in f:
		numlineas = numlineas+1

medidas = np.empty([numlineas,3])
timeStampsArray = ["" for x in range(numlineas)]
#timeStampsDT = []

i=0
with open('torreME_editado.txt','r') as f:
    for line in f:
		lineaArray = line.split()
		if len(lineaArray)==6:
			timeStampsArray[i]=lineaArray[0]+" "+lineaArray[1]
			medidas[i,:] = [float(lineaArray[3]),float(lineaArray[4]),float(lineaArray[5])]			
			#d=datetime.datetime.strptime(lineaArray[0]+" "+lineaArray[1], "%d/%m/%Y %H:%M:%S")
			##timeStampsDT.append(d)
			#timeStampsDT[i]=d
			
			#datos40m = [datos['medidas'][i][0] for i in range(len(datos['medidas']))]
			#print "First number is {} and second number is {}".format(len(timeStampsArray), len(medidas))
			if len(timeStampsArray)!=len(medidas):
				print(i)
		i=i+1
	
savemat('torreME_editado.mat',dict(medidas=medidas,timeStamps=timeStampsArray))



