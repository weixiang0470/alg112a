from datetime import datetime

n=25
#n=100
# 方法 1
def power2n_m1(n):
    return 2**n

# 方法 2a：用遞迴
def power2n_m2(n):
    if n==0:
        return 1
    return power2n_m2(n-1)+power2n_m2(n-1)

# 方法2b：用遞迴
def power2n_m3(n):
    if n==0:
        return 1
    return 2*power2n_m3(n-1)

# 方法 3：用遞迴+查表
arr = [None]*1000
def power2n_m4(n):
    if n==0:
        return 1
    if arr[n]!=None:
        return arr[n]
    else:
        arr[n] = power2n_m4(n-1)+power2n_m4(n-1)
    return arr[n]
    # if ....
    # power2n(n-1)+power2n(n-1) 

print('')
stime = datetime.now()
print(f'power2n_m1({n}) : {power2n_m1(n)}')
etime = datetime.now()
print(f'time : {etime-stime}')
print('---------------------------')

stime = datetime.now()
print(f'power2n_m2({n}) : {power2n_m2(n)}')
etime = datetime.now()
print(f'time : {etime-stime}')
print('---------------------------')

stime = datetime.now()
print(f'power2n_m3({n}) : {power2n_m3(n)}')
etime = datetime.now()
print(f'time : {etime-stime}')
print('---------------------------')

stime = datetime.now()
print(f'power2n_m4({n}) : {power2n_m4(n)}')
etime = datetime.now()
print(f'time : {etime-stime}')
print('')