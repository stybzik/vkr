import csv
import numpy as np
from numpy import histogram
from sympy import *
from scipy.stats import kstest
import os


a, b, x = symbols('a b x')
Price = []
#1.00054100832 0.0228230832541 day
#1.00290208247 0.0560470621315 week
#1.01056258987 0.0884489808817 mounth
#SBER_090301_170301_m
#RI.MICEX LC  _090301_170301_m
with open(os.path.join('data', 'SBER_090301_170301_w.csv')) as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        Price.append(float(row['<CLOSE>']))
S = []
N = len(Price)-1
print('# viborki = ', N)
for i in range(N):
    S.append(round(ln(Price[i + 1]/Price[i]), 12))
E = np.mean(np.array(S))
sko = np.var(np.array(S)) ** 0.5
print('mean = ', E)
print('sko = ', sko)

#f = 1 / ((2 * pi) ** 0.5) * exp (- x ** 2 / 2)
f = (1 / (sko * ((2 * pi) ** 0.5))) * exp ((- (x - E) ** 2 )/ (2 * sko ** 2))
'''teta = sko ** 2 / E
k = E / teta
print(k, teta)
G = integrate(x ** (k-1) * exp (-x), (x, 0, +oo))
print(G)
f = (x ** (k - 1) * exp(-x / teta)) / (teta ** k * G)'''
BIN = []
for i in range(36):
    BIN.append(E - (18 - i) * sko / 6)
print('otrezki = ', BIN)
EMPIR = histogram(S, bins = BIN)[0]
print('empiricheskie = ', EMPIR)
print('min = ', np.min(np.array(S)))
print('max = ', np.max(np.array(S)))
TEOR = []
Answer = 0
for i in range(len(BIN)-1):
    a = BIN[i]
    b = BIN[i + 1]
#    print(a, b)
    TEOR.append(float(integrate(f ,(x, a, b))))
    print(N * TEOR[i], end =' ')
    Answer += N * ((EMPIR[i] / N - TEOR[i]) ** 2 )/ TEOR[i]
print('teoreticheskie = ', TEOR)
print('minimum = ', N * min(TEOR))
print('kriterij = ', Answer)
print('stepeni svobodi = ', len(TEOR)-3)
print('*Kolmogorov*')
test = kstest(S, 'norm')
print(test)
