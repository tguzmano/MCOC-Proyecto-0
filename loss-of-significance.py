# -*- coding: utf-8 -*-
"""
Created on Tue Jul 31 14:24:36 2018

@author: Tomás
"""

from numpy import *
import numpy as np


#El siguiente procedimiento se repite para matrices de 2x2, 4x4, 8x8, 16x16 y 32x32.


#Se crea matriz de 2x2
datos = np.random.randn(2, 2)
#Se obtienen componentes de la matriz con float 32
datos_32 = array((datos), dtype=np.float32)
#Se obtienen componentes de la matriz con float 64
datos_64 = array((datos), dtype=np.float64)

#Se calculan determinantes para cada float
det = linalg.det(datos)
det_32 = linalg.det(datos_32)
det_64 = linalg.det(datos_64)

print det_32
print det_64

#Calculo del error para float 32
resta = (det_32 - det)
error_32 = (abs(resta) / abs(det)) * 100

#Calculo del error para float 64
resta = (det_64 - det)
error_64 = (abs(resta) / abs(det)) * 100

print error_32
print error_64



#Se crea matriz de 4x4
datos2 = np.random.randn(4, 4)
datos2_32 = array((datos2), dtype=np.float32)
datos2_64 = array((datos2), dtype=np.float64)

det2 = linalg.det(datos2)
det2_32 = linalg.det(datos2_32)
det2_64 = linalg.det(datos2_64)

print det2_32
print det2_64

resta2 = (det2_32 - det2)
error2_32 = (abs(resta2) / abs(det2)) * 100

resta2 = (det2_64 - det2)
error2_64 = (abs(resta2) / abs(det2)) * 100

print error2_32
print error2_64



#Se crea matriz de 8x8
datos3 = np.random.randn(8, 8)
datos3_32 = array((datos3), dtype=np.float32)
datos3_64 = array((datos3), dtype=np.float64)

det3 = linalg.det(datos3)
det3_32 = linalg.det(datos3_32)
det3_64 = linalg.det(datos3_64)

print det3_32
print det3_64

resta3 = (det3_32 - det3)
error3_32 = (abs(resta3) / abs(det3)) * 100

resta3 = (det3_64 - det3)
error3_64 = (abs(resta3) / abs(det3)) * 100

print error3_32
print error3_64



#Se crea matriz de 16x16
datos4 = np.random.randn(16, 16)
datos4_32 = array((datos4), dtype=np.float32)
datos4_64 = array((datos4), dtype=np.float64)

det4 = linalg.det(datos4)
det4_32 = linalg.det(datos4_32)
det4_64 = linalg.det(datos4_64)

print det4_32
print det4_64

resta4 = (det4_32 - det4)
error4_32 = (abs(resta4) / abs(det4)) * 100

resta4 = (det4_64 - det4)
error4_64 = (abs(resta4) / abs(det4)) * 100

print error4_32
print error4_64



#Se crea matriz de 32x32
datos5 = np.random.randn(32, 32)
datos5_32 = array((datos5), dtype=np.float32)
datos5_64 = array((datos5), dtype=np.float64)

det5 = linalg.det(datos5)
det5_32 = linalg.det(datos5_32)
det5_64 = linalg.det(datos5_64)

print det5_32
print det5_64

resta5 = (det5_32 - det5)
error5_32 = (abs(resta5) / abs(det5)) * 100

resta5 = (det5_64 - det5)
error5_64 = (abs(resta5) / abs(det5)) * 100

print error5_32
print error5_64