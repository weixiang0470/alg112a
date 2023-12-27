def neighbours(x,y,maze):
    nb_list = []
    if x-1 >= 0 and maze[x-1][y] == "0": 
        nb = [x-1,y]
        nb_list.append(nb)
    if x+1 <= 5 and maze[x+1][y] == "0":
        nb = [x+1,y]
        nb_list.append(nb)
    if y-1 >= 0 and maze[x][y-1] == "0":
        nb = [x,y-1]
        nb_list.append(nb)
    if y+1 <= 7 and maze[x][y+1] == "0":
        nb = [x,y+1]
        nb_list.append(nb)
    return nb_list

def dfs(p,path,visitedMap,maze):
    global final
    x,y=p[0],p[1]
    m2=Modify_maze(x,y,maze)
    P_maze(m2)
    if x>5 or y>7 : return 
    if x==5 and y==5 : 
        path.append(p)
        final = path.copy()
        return
    p_str= ''.join(str(p))
    if visitedMap.get(p_str):return
    visitedMap[p_str] = True
    path.append(p)
    for nb in neighbours(x,y,m2):
        dfs(nb,path,visitedMap,m2)
    path.pop()

def P_maze(maze):
    for i in maze:
        print(i)
    print("========")

def Modify_maze(x,y,maze):
    m2=[]
    for i in range(len(maze)):
        s=""
        for j in range(len(maze[i])):
            if(i==x and j==y and maze[i][j]=="0"):s+="x"
            else: s+=maze[i][j]
        m2.append(s)
    return m2

maze = ["11111111",
        "11010111",
        "00000111",
        "10111111",
        "10000011",
        "11111011"]
visitedMap={}
path=[]
p=[2,0]
final=[]
dfs(p,path,visitedMap,maze)
print(f'Path : {final}')