Size = 8
count=0
board = [[0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0]]

def B_print(board):
    for row in board:
        print(row)

def Is_Safe(row,col):
    for r in range(row):
        if board[r][col]==1:return 0
    
    c=col
    for r in range(row-1,-1,-1):
        c-=1
        if c<0: break
        if board[r][c]==1:return 0

    c=col
    for r in range(row-1,-1,-1):
        c+=1
        if c>=Size: break
        if board[r][c]==1:return 0
    return 1

def dfs(row):
    global count
    #print('board:')
    #B_print(board)
    if row==Size: 
        count+=1
        print(f'Solution {count} :')
        B_print(board)
        return 1
    for c in range(Size):
        if (Is_Safe(row,c)):
            board[row][c]=1
            #B_print(board)
            dfs(row+1)
            board[row][c]=0


dfs(0)