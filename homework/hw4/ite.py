f1 = lambda x : (3*x - 1)/x 
f2 = lambda x : x - 0.125 * (1 - (3/x) + (1/x**2))
f3 = lambda x : 0.99*x + 3/100*(x**2) - (x**3)/100
#f4 = lambda x : (x**2 + 1)/3
#f5 = lambda x : (x-1)**2
#f6 = lambda x : x/(x-1) +1
f7 = lambda x : x + 0.01*(x**2 - 3*x + 1)

x1 = x2 = 5
x3 =3
#x4=x5=x6= 2
x7=1

for i in range(1000):
    x1,x2,x3 = f1(x1),f2(x2),f3(x3)
    x7 = f7(x7)
    #x4,x5,x6 = f4(x4),f5(x5),f6(x6)
    print(f'x1:{x1} | x2:{x2} | x3:{x3} | x7:{x7}')
    #print(f'x4:{x4} | x5:{x5} | x6:{x6}')
