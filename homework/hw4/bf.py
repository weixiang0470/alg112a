from numpy import arange

def f(x):
    return (x**2) - (3*x) +1

for x in arange(-100, 100, 0.001):
    if abs(f(x)) < 0.001:
        print("x=", x, " f(x)=", f(x)) 