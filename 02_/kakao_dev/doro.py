from pprint import pprint


import copy
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
M = 999999999

def dfs(r, c, d,m, a,b):
    global M
    if m>M:
        return
    if r==a-1 and c==b-1:
        if m<M:
            M=m
        return 
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<a and 0<=nc<b:
            if arr[nr][nc] == 0:
                if i==d:
                    arr[nr][nc]=2
                    dfs(nr, nc, i, m+100,a,b)
                    arr[nr][nc]=0
                else:
                    arr[nr][nc]=2
                    dfs(nr, nc, i, m+600,a,b)
                    arr[nr][nc]=0

def solution(board):
    global arr
    x, y = len(board), len(board[0])
    arr = board
    for i in range(1,3):
        # x = copy.deepcopy(board)
        board[0][0]=2
        dfs(0,0,i,0,x,y)
    return M



sample = [[0,0,1,0],[0,0,0,0],[0,1,0,1],[1,0,0,0]]	
print(solution(sample))