from numpy import random
outfile = open('random.csv', 'w')
k = 2.7
teta = 0.43
Len = 1000
E = 1.01056258987
sko = 0.0884489808817
print('hello')
for i in range(Len):
    g = random.lognormal(E, sko)
    outfile.write(str(g))
    outfile.write('\n')
outfile.close()
print('E =', k * teta)
print('sko =', (k * teta ** 2) ** 0.5)
