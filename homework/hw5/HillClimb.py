import random

def neighbor(f,p,h):
    i = len(p)
    start = 0
    p1 = p.copy()
    while(start < i):
        p1[start] += random.uniform(-h,h)
        start += 1 
    f1 = f(p1)
    #if(f1 >= f(p)):
    #   p = p1.copy()
    return p1 , f1

def hillClimbing(f, p, h=0.01):
    failCount = 0                    # 失敗次數歸零
    while (failCount < 10000):       # 如果失敗次數小於一萬次就繼續執行
        fnow = f(p)                  # fxy 為目前高度
        p1, f1 = neighbor(f, p, h)
        if f1 >= fnow:               # 如果移動後高度比現在高
            fnow = f1                #   就移過去
            p = p1
            print('p=', p, 'f(p)=', fnow)
            failCount = 0            # 失敗次數歸零
        else:                        # 若沒有更高
            failCount = failCount + 1#   那就又失敗一次
    return p,fnow                 # 結束傳回 （已經失敗超過一萬次了）

def f(p):
    #return -1 * ( x*x -2*x + y*y +2*y - 8 )
    return -1*(p[0]**2+p[1]**2+p[2]**2)

p_f , fnow_f = hillClimbing(f, [2,1,3])

print(f'p = {p_f}')
print(f'f = {fnow_f}')