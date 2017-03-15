from sympy import *
import numpy as np
'''import matplotlib.pyplot as plt
'''
a, l, m, r = symbols('A L M r')
#M = -9
s = 1.04
mu = 0.02
lam = 0.02
'''R = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15]
P = [0.0078, 0.0086, 0.0093, 0.0101, 0.0108, 0.0115, 0.0123, 0.0131, 0.0138, 0.0146, 0.0153, 0.016, 0.0168, 0.0175, 0.0183, 0.019, 0.0198, 0.0205, 0.0213, 0.022, 0.0228, 0.0235, 0.0243, 0.0251, 0.0258, 0.0265, 0.0272, 0.028, 0.0287, 0.0295, 0.4402]
'''
R = [0.85, 1.15]
P = [0.25, 0.75]
n = len(R)
def f(M):
    F = ((1 - a - (1 + lam) * l + (1 - mu) * m) * s + (a + l - m) * r) ** M
    F1 = diff(F.subs(m, 0), l).subs(l, 0)
    F2 = diff(F.subs(l, 0), m).subs(m, 0)
    F11 = 0
    F22 = 0
    for i in range(n):
        F11 += P[i] * F1.subs(r, R[i])
        F22 += P[i] * F2.subs(r, R[i])
    A = 1
    B = -1
    while abs(A-B)>0.001:
        A = A - (F11.subs(a, A)*(B-A))/(F11.subs(a, B)-F11.subs(a, A))
        B = B - F11.subs(a, B)/diff(F11, a).subs(a, B)
    A1 = (A + B) / 2
    A = 1
    B = -1
    while abs(A-B)>0.001:
        A = A - (F22.subs(a, A)*(B-A))/(F22.subs(a, B)-F22.subs(a, A))
        B = B - F22.subs(a, B)/diff(F22, a).subs(a, B)
    A2 = (A + B) / 2
    if A1 < 0:
        A1 = 0
    elif A1 > 1:
        A1 = 1
    if A2 < 0:
        A2 = 0
    elif A2 > 1:
        A2 = 1
#    print(A1, A2)
    return([A1, A2])
Num = 59
axes = [0] * Num
boder = [0] * Num
boder2 = [0] * Num
for i in range(Num):
    print(i)
    t = (i+1)*0.003
    axes[i] = t
    [boder[i], boder2[i]] = f(t)
print (axes)
print(boder2)
print(boder)

"""fig = plt.figure()
ax1 = fig.add_subplot(111)
plt.xlabel('axes')
plt.ylabel('bode')
ax1.plot(axes, boder, lw=3, color='#dd2222')
ax1.plot(axes, boder2, lw=3, color='#22ff22')
#ax1.fill_between(axes, boder, 1, facecolor='#ff8888')
plt.show()"""
