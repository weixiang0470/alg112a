arr=[]
def truthtable(arr,n):
    l = len(arr)
    if l == n:
        print(arr)
        return
    for element in [0,1]:
        arr.append(element)
        truthtable(arr,n)
        arr.pop()

truthtable(arr,2)
truthtable(arr,3)
truthtable(arr,4)