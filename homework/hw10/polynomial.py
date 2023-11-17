def f(x):
    return x**5 +1
    #return x**8 + 3*(x**2) + 1

def neighbour(x,h):
    nb_list=[]
    x2=x+h
    x3=x-h
    nb_list.append(x2)
    nb_list.append(x3)
    return nb_list

def dfs(x,failCount,visitedMap,Ans):
    x_str=str(x)
    if visitedMap.get(x_str): return
    visitedMap[x_str] = True
    #print(f'x:{x} , f(x):{f(x)} FC:{failCount}')
    if f(x) > -0.001 and f(x) < 0.001 : 
        aannss = f'x:{x} f(x):{f(x)}'
        Ans.append(aannss)
        return
    if failCount > 900 : 
        failCount=0
        return
    failCount+=1
    nb_list = neighbour(x,0.01)
    for nb in range(len(nb_list)):
        dfs(nb_list[nb],failCount,visitedMap,Ans)
visitedMap={}
Ans=[]
dfs(0,0,visitedMap,Ans)
if not Ans:
    print("No solution")
else :
    for ans in Ans:
        print(ans)