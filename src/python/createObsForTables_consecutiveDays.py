#!/usr/bin/python

import sys
import numpy as np
import pickle
import pandas as pd
import datetime
from scipy.io import savemat
from datetime import timedelta



with open('serie_viento.pickle','r') as f:
	#viento = pickle.load(f)
    viento = pd.read_pickle('serie_viento.pickle')


vientoHorario=viento.asfreq('1h')

wStart = int(sys.argv[1])
wEnd = int(sys.argv[2])

h = int(sys.argv[3])

resultDict = {}
horizon = timedelta(hours=h)
oneDay = timedelta(hours=24)
for wSizeCount in range(wStart,wEnd+1):
    i=0
    inputs = np.ndarray(shape=(wSizeCount,len(vientoHorario)))
    outputs = np.ndarray(len(vientoHorario))
    for index,value in vientoHorario.iteritems():
        try:
            if (index+(wSizeCount*oneDay)+horizon<=vientoHorario.index[-1]):
                inputs[:,i] = vientoHorario[index:index+(wSizeCount-1)]
                outputs[i] =  vientoHorario[index+wSizeCount+horizon]
                i=i+1
        except KeyError:
            print("Esto no deberia ocurrir, ya que se controla con el if. Indice: %s"%index)
        except ValueError:
            print("A partir de este indice ya no hay suficientes valores para tener una ventana completa: %s"%index)
            break
    inputs = inputs[:,0:i]
    outputs = outputs[0:i]
    resultDict['k_'+str(wSizeCount)+'_inputs'] = inputs
    resultDict['k_'+str(wSizeCount)+'_outputs'] = outputs

savemat('data_consecutiveDays'+'_wStart'+str(wStart)+'_wEnd'+str(wEnd)+'_h'+str(h),resultDict)

