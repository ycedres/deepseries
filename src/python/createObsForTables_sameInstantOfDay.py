#!/usr/bin/python

import sys
import numpy as np
import pandas as pd
import pickle
from scipy.io import savemat
from datetime import timedelta

with open('serie_viento.pickle','r') as f:
	#viento = pickle.load(f)
    viento = pd.read_pickle('serie_viento.pickle')

vientoHorario=viento.asfreq('1h')

wStart = int(sys.argv[1])
wEnd = int(sys.argv[2])

h = int(sys.argv[3])
horizon = timedelta(hours=h)

oneDay = timedelta(hours=24)
resultDict = {}


for wSizeCount in range(wStart,wEnd+1):
    i=0
    inputs = np.ndarray(shape=(wSizeCount,len(vientoHorario)))
    outputs = np.ndarray(len(vientoHorario))
    for index,value in vientoHorario.iteritems():
        try:
            if (index+oneDay*(wSizeCount-1)+horizon<=vientoHorario.index[-1]):
                for j in range(0,wSizeCount):
                    inputs[j,i] = vientoHorario[index+oneDay*j]
                outputs[i] = vientoHorario[index+oneDay*(wSizeCount-1)+horizon]
                i=i+1
            else:
                break
        except ValueError:
            print("A partir de este indice ya no hay suficientes valores para tener una ventana completa: %s"%index)
            break
        except KeyError:
            print(index)
            print("KeyError: i:%s,j:%s"%(i,j))
            break
        except IndexError:
            print(index)
            print("IndexError: i:%s,j:%s"%(i,j))
            break

    inputs = inputs[:,0:i]
    outputs = outputs[0:i]

    resultDict['k_'+str(wSizeCount)+'_inputs'] = inputs
    resultDict['k_'+str(wSizeCount)+'_outputs'] = outputs


savemat('data_sameInstantOfDay'+'_wStart'+str(wStart)+'_wEnd'+str(wEnd)+'_h'+str(h),resultDict)
