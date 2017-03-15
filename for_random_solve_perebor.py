from sympy import *
from numpy import random

a, l, m, r = symbols('A L M r')
M = -8
s = 1.051 ** (1 / 12)
mu = 0.0005
lam = 0.0005
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
    N = 5000
    for i in range(N):
        print(i)
        z = random.lognormal(0.0210579525465, 0.108943832524, 2)
        FUNbuy = funbuy.subs(r, z[0])
        FUNsell = funsell.subs(r, z[1])
        MINbuy = abs(FUNbuy.subs(a, 0))
        MINsell = abs(FUNsell.subs(a, 0))
        bodersell = 0
        boderbuy = 0
        k = 0
        while k < 1:
            k += 0.01
            ybuy = abs(FUNbuy.subs(a, k))
            ysell = abs(FUNsell.subs(a, k))
            if MINbuy >= ybuy:
                boderbuy = k
                MINbuy = ybuy
            if MINsell >= ysell:
                bodersell = k
                MINsell = ysell
        lsell += bodersell
        lbuy += boderbuy
    return(lbuy/N, lsell/N)



UP, DOWN = border(1)
print(UP[::-1])
print(DOWN[::-1])
