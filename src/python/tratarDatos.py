#!/usr/bin/python

from scipy.io import loadmat
import pandas
import datetime
import pickle

datos = loadmat('torreME_editado.mat')

datos40m = [datos['medidas'][i][0] for i in range(len(datos['medidas']))]
tmp2 = [datetime.datetime.strptime(d, "%d/%m/%Y %H:%M:%S") for d in datos['timeStamps']]
tmp = pandas.Series(datos40m,index=tmp2)


with open('serie_viento.pickle', 'wb') as handle:
      pickle.dump(tmp, handle)



#for idx,dato in enumerate(datos['timeStamps']):
#	if dato=='                   ':
#		print idx

#11521
#39368
#Los elimino a mano del fichero

#fecha1=datetime.datetime.strptime("23/07/2004 08:02:00", "%d/%m/%Y %H:%M:%S")
#fecha2=datetime.datetime.strptime("24/07/2004 08:02:00", "%d/%m/%Y %H:%M:%S")
#tmp[fecha1:fecha2]
