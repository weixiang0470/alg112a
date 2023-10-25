p=[]

def permutation(n,p):
    l=len(p)
    if l == n:
        print(p)
        return
    else:
        for x in range(n):
            if not x in p:
                p.append(x)
                #print(f'trace:{p}')
                permutation(n,p)
                p.pop()
                #print(f'trace2:{p}')

permutation(2,p)
permutation(3,p)
#permutation(4,p)
