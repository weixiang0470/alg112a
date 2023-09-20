from datetime import datetime
stime = datetime.now()

arr = [None]*1000
n=60
arr[0]=0
arr[1]=1

if n>=2 :
    tmp = 2
    while tmp <= n:
        arr[tmp] = arr[tmp-1] + arr[tmp-2]
        tmp+=1

print(f'fibonacci({n}) = {arr[n]}')
etime = datetime.now()
print(f'time:{etime-stime}')