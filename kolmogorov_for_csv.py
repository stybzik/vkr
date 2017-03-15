from math import log
from scipy.stats import kstest

outfile = open('random.csv', 'r')
s = []
for i in outfile:
    s.append(log(float(i)))
#print(s)
test = kstest(s, 'norm')
print(test)
