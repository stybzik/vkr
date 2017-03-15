from numpy import histogram
from sympy import *



a, b, x = symbols ('a b x')
outfile = open('random.csv', 'r')
s = []
for i in outfile:
    s.append(float(i))
#print(s)
N = 1000
E = 1.01056258987
sko = 0.0884489808817
BIN = []
for i in range(6):
    BIN.append(E - (1.5 - i) * sko)
print('otrezki = ', BIN)
EMPIR = histogram(s, bins = BIN)[0]

TEOR = []
Answer = 0
for i in range(len(BIN)-1):
    a = ln(BIN[i])
    b = ln(BIN[i + 1])
    print(a, b)
    TEOR.append(integrate((1 / (sko * (2 * pi) ** 0.5)) * exp (- (x - E) ** 2 / (2 * sko ** 2)) ,(x, a, b)))
    Answer += N * ((EMPIR[i] / N - TEOR[i]) ** 2 )/ TEOR[i]
print('teoreticheskie = ', TEOR)
print('minimum = ', N * min(TEOR))
print('kriterij = ', Answer)
print('stepeni svobodi = ', len(TEOR)-3)

'''a = []
b = []
a, b = histogram(s, )
print(a)'''
