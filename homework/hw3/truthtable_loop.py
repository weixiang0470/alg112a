def decimalToBinary(n):
    return "{0:b}".format(int(n))

def D_2_2D(arr):
    arr1=[]
    while len(arr) > 0:
        arr1.append(arr.pop())
    while len(arr1) >0:
        print(arr1.pop())

def truthtable(n):
    arr=[]
    num = 2**n
    for x in range(0,num):
        y = decimalToBinary(x)
        arr.append(y)
        tmp=""
        if(len(arr[x]) < n):
            for z in range(0,n-1):
                tmp += "0"
                tmp2 = tmp + arr[x]
                if(len(tmp2) == n):break
            tmp+=arr[x]
            arr.pop()
            arr.append(tmp)
            #print('tmp=',tmp)
            #print(arr)
    print(f'{n} digit truth table :')
    D_2_2D(arr)
#print(decimalToBinary(0))
#print(decimalToBinary(1))
#print(decimalToBinary(2))
#print(decimalToBinary(3))
truthtable(2)
truthtable(3)
truthtable(4)

