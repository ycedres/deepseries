#!/usr/bin/python

import os

# Forecast horizon 24 hours
for i in range(24,73):
    os.system('./generarConjuntos.py'+ ' ' + str(i) + ' ' + str(24) + ' ' + 'windData_WinSizeDaysInaRow_v24_h24.mat') #Poner nombre de fichero

#os.system('./generarConjuntos.py'+ ' ' + str(24) + ' ' + str(24) + ' ' + 'windData_WinSizeDaysInaRow_v24_h24.mat') #Poner nombre de fichero
#os.system('./generarConjuntos.py'+ ' ' + str(48) + ' ' + str(24) + ' ' + 'windData_WinSizeDaysInaRow_v48_h24.mat') #Poner nombre de fichero
#os.system('./generarConjuntos.py'+ ' ' + str(72) + ' ' + str(24) + ' ' + 'windData_WinSizeDaysInaRow_v72_h24.mat') #Poner nombre de fichero

for i in range(24,73):
    os.system('./createObservationsForecastSets.py' + ' ' + str(i) + ' ' + str(24) + ' ' + 'windData_sameInstantOfDay_w12_h24.mat')

#os.system('./createObservationsForecastSets.py' + ' ' + str(48) + ' ' + str(24) + ' ' + 'windData_sameInstantOfDay_w12_h24.mat')
#os.system('./createObservationsForecastSets.py' + ' ' + str(72) + ' ' + str(24) + ' ' + 'windData_sameInstantOfDay_w12_h24.mat')

