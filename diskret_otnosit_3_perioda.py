from sympy import *
a, l, m, r = symbols('A L M r')
M = -5
s = 1.04
mu = 0.02
lam = 0.02
R = [0.85, 1.15]
P = [0.25, 0.75]
n = len(R)
a1 = [0]*4
a2 = [0]*4
F = ((1 - a - (1 + lam) * l + (1 - mu) * m) * s + (a + l - m) * r) ** M
F1 = diff(F.subs(m, 0), l).subs(l, 0)
F2 = diff(F.subs(l, 0), m).subs(m, 0)
F11 = 0
F22 = 0
for i in range(n):
    F11 += P[i] * F1.subs(r, R[i])
    F22 += P[i] * F2.subs(r, R[i])
A = 1
B = 0
while abs(A-B)>0.001:
    A = A - (F11.subs(a, A)*(B-A))/(F11.subs(a, B)-F11.subs(a, A))
    B = B - F11.subs(a, B)/diff(F11, a).subs(a, B)
A1 = (A + B) / 2
A = 1
B = 0
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
a1[0] = A1
a2[0] = A2
Jbue = (F.subs(m, 0)) * (F.subs(m, 0).subs(a, (r - s) * (a + (1 + lam) * l)))
Jbue1 = diff(Jbue, l).subs(l, 0)
Jsell = (F.subs(l, 0)) * F.subs(l, 0).subs(a, (r - s) * (a - (1 - mu) * m))
Jsell1 = diff(Jsell, m).subs(m, 0)
Jsell11 = 0
Jbue11 = 0
for i in range(n):
    Jsell11 += P[i] * Jsell1.subs(r, R[i])
    Jbue11 += P[i] * Jbue1.subs(r, R[i])
A = 1
B = -1
while abs(A-B)>0.05:
    A = A - (Jbue11.subs(a, A)*(B-A))/(Jbue11.subs(a, B)-Jbue11.subs(a, A))
    B = B - Jbue11.subs(a, B)/diff(Jbue11, a).subs(a, B)
A11 = (A + B) / 2
A = 1
B = -1
while abs(A-B)>0.05:
    A = A - (Jsell11.subs(a, A)*(B-A))/(Jsell11.subs(a, B)-Jsell11.subs(a, A))
    B = B - Jsell11.subs(a, B)/diff(Jsell11, a).subs(a, B)
A22 = (A + B) / 2
if A11 < 0:
    A11 = 0
elif A11 > 1:
    A11 = 1
if A22 < 0:
    A22 = 0
elif A22 > 1:
    A22 = 1
a1[1] = A11
a2[1] = A22
R = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15]
P = [0.0078, 0.0086, 0.0093, 0.0101, 0.0108, 0.0115, 0.0123, 0.0131, 0.0138, 0.0146, 0.0153, 0.016, 0.0168, 0.0175, 0.0183, 0.019, 0.0198, 0.0205, 0.0213, 0.022, 0.0228, 0.0235, 0.0243, 0.0251, 0.0258, 0.0265, 0.0272, 0.028, 0.0287, 0.0295, 0.4402]
n = len(R)
Jbue = Jbue.subs(a, (r - s) * (a + (1 + lam) * l)) * F.subs(m, 0)
Jbue1 = diff(Jbue, l).subs(l, 0)
Jsell = F.subs(l, 0) * Jsell.subs(a, (r - s) * (a - (1 - mu) * m))
Jsell1 = diff(Jsell, m).subs(m, 0)
Jsell11 = 0
Jbue11 = 0
for i in range(n):
    Jsell11 += P[i] * Jsell1.subs(r, R[i])
    Jbue11 += P[i] * Jbue1.subs(r, R[i])
A = 1
B = -1
while abs(A-B)>0.001:
    A = A - (Jbue11.subs(a, A)*(B-A))/(Jbue11.subs(a, B)-Jbue11.subs(a, A))
    B = B - Jbue11.subs(a, B)/diff(Jbue11, a).subs(a, B)
A11 = (A + B) / 2
A = 1
B = -1
while abs(A-B)>0.05:
    A = A - (Jsell11.subs(a, A)*(B-A))/(Jsell11.subs(a, B)-Jsell11.subs(a, A))
    B = B - Jsell11.subs(a, B)/diff(Jsell11, a).subs(a, B)
A22 = (A + B) / 2
if A11 < 0:
    A11 = 0
elif A11 > 1:
    A11 = 1
if A22 < 0:
    A22 = 0
elif A22 > 1:
    A22 = 1
a1[2] = A11
a2[2] = A22
R = [0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13]
P = [0.024, 0.0252, 0.0264, 0.0277, 0.029, 0.0306, 0.0322, 0.0339, 0.0359, 0.0381, 0.0407, 0.0436, 0.0472, 0.0508, 0.0553, 0.0603, 0.0663, 0.3328]
n = len(R)
'''
R = [0.85, 0.86, 0.87, 0.88, 0.89, 0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1, 1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1, 1.11, 1.12, 1.13, 1.14, 1.15]
P = [0.0078, 0.0086, 0.0093, 0.0101, 0.0108, 0.0115, 0.0123, 0.0131, 0.0138, 0.0146, 0.0153, 0.016, 0.0168, 0.0175, 0.0183, 0.019, 0.0198, 0.0205, 0.0213, 0.022, 0.0228, 0.0235, 0.0243, 0.0251, 0.0258, 0.0265, 0.0272, 0.028, 0.0287, 0.0295, 0.4402]
n = len(R)
'''
Jbue = Jbue.subs(a, (r - s) * (a + (1 + lam) * l)) * F.subs(m, 0)
Jbue1 = diff(Jbue, l).subs(l, 0)
Jsell = F.subs(l, 0) * Jsell.subs(a, (r - s) * (a - (1 - mu) * m))
Jsell1 = diff(Jsell, m).subs(m, 0)
Jsell11 = 0
Jbue11 = 0
for i in range(n):
    Jsell11 += P[i] * Jsell1.subs(r, R[i])
    Jbue11 += P[i] * Jbue1.subs(r, R[i])
A = 1
B = -1
while abs(A-B)>0.001:
    A = A - (Jbue11.subs(a, A)*(B-A))/(Jbue11.subs(a, B)-Jbue11.subs(a, A))
    B = B - Jbue11.subs(a, B)/diff(Jbue11, a).subs(a, B)
A11 = (A + B) / 2
A = 1
B = -1
while abs(A-B)>0.05:
    A = A - (Jsell11.subs(a, A)*(B-A))/(Jsell11.subs(a, B)-Jsell11.subs(a, A))
    B = B - Jsell11.subs(a, B)/diff(Jsell11, a).subs(a, B)
A22 = (A + B) / 2
if A11 < 0:
    A11 = 0
elif A11 > 1:
    A11 = 1
if A22 < 0:
    A22 = 0
elif A22 > 1:
    A22 = 1
a1[3] = A11
a2[3] = A22
a1 = a1[::-1]
a2 = a2[::-1]
print(a2)
print(a1)

