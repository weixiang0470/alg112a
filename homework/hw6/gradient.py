step = 0.01

# 函數 f 對變數 p[k] 的偏微分: df / dp[k]
def df(f, p, k):
    p1 = p.copy()
    p1[k] = p[k]+step
    return (f(p1) - f(p)) / step

# 梯度：函數 f 在點 p 上的梯度
def grad(f, p):
    gp = p.copy()
    for k in range(len(p)):
        gp[k] = df(f, p, k)
    return gp

def f(p):
    #return  ( p[0]*p[0] -2*p[0] + p[1]*p[1] - 2*p[1] - 8 )
    #return -1*(p[0]**2+p[1]**2+p[2]**2)
    return (p[0]-1)**2 + (p[1]-2)**2 + (p[2]-3)**2

def descent(gp,p):
    p_new = p.copy()
    for i in range(len(p_new)):
        p_new[i] += gp[i] * (-1) * step 
    return p_new

if __name__ == "__main__" :
    p = [-3,-3,0]
    fail = 10000
    flat = len(p)
    count=0
    #print(f'grad : {grad(f,p)}')
    while(fail>0):
        if count == flat: #If all vector in gp are 0 then break
            break
        fail -= 1
        count = 0
        gp = grad(f,p)
        p_new = descent(gp,p)
        diff = f(p) - f(p_new)
        if diff < 0.0000001: break 
        p = p_new.copy()
        print(f'grad : {grad(f,p)} | point : {p}')
        for j in range(flat):
            if gp[j] <= 0.01 and gp[j] >= 0.01: #if vertor of gp is zero count++
                count += 1
