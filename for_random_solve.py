from sympy import *
from numpy import random

a, l, m, r = symbols('A L M r')
M = 0.3
s = 1.03 ** (1 / 52)
mu = 0.015
lam = 0.015
F = ((1 - a - (1 + lam) * l + (1 - mu) * m) * s + (a + l - m) * r) ** M
Fbuy = F.subs(m, 0)
Fsell = F.subs(l, 0)

def border(n):
    global Fbuy
    global Fsell
    down = [0] * n
    up = [0] * n
    for t in range(n):
        print(t+1, '=='*42)
        if t > 0:
            Fbuy = Fbuy * (Fbuy.subs(a, (r - s) * (a + (1 + lam) * l)))
            Fsell = Fsell * (Fsell.subs(a, (r - s) * (a - (1 - mu) * m)))
        Jbuy = diff(Fbuy, l).subs(l, 0)
        Jsell = diff(Fsell, m).subs(m, 0)
        down[t], up[t] = immod(Jbuy, Jsell)
    return up, down

def immod(funbuy, funsell):
    lbuy = 0
    lsell = 0
    N = 10000
    for i in range(N):
        print(i)
        z = random.lognormal(0.00571136544243, 0.0511839259556, 2)
        FUNbuy = funbuy.subs(r, z[0])
        FUNsell = funsell.subs(r, z[1])
        A = FUNbuy.subs(a, 0)
        B = FUNbuy.subs(a, 1)
        if A * B >= 0:
            if abs(A) > abs(B):
                boderbuy = 1
            else:
                boderbuy = 0
        else:
            x = 0
            y = 1
            while (abs(x - y) > 0.0001):
                v = (x + y) / 2
                if FUNbuy.subs(a, x) * FUNbuy.subs(a, v) < 0:
                    y = v
                else:
                    x = v
            boderbuy = (x + y) / 2
        A = FUNsell.subs(a, 0)
        B = FUNsell.subs(a, 1)
        if A * B >= 0:
            if abs(A) > abs(B):
                bodersell = 1
            else:
                bodersell = 0
        else:
            x = 0
            y = 1
            while (abs(x - y) > 0.0001):
                v = (x + y) / 2
                if FUNsell.subs(a, x) * FUNsell.subs(a, v) < 0:
                    y = v
                else:
                    x = v
            bodersell = (x + y) / 2
        lsell += bodersell
        lbuy += boderbuy
    return(lbuy/N, lsell/N)



UP, DOWN = border(1)
print(UP[::-1])
print(DOWN[::-1])
