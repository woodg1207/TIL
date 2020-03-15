from pprint import pprint
dr=[0,1,0,-1]
dc=[1,0,-1,0]
arr = [[False]*5 for _ in range(5)]
def dfs(r, c, d, cnt):
    d = d%4
    if not arr[r][c]:
        # print(r,c)
        arr[r][c] = cnt
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<5 and 0<=nc<5:
            if arr[nr][nc]==0:
                dfs(nr, nc, d,cnt+1)
            else:
                x = (d+1)%4
                nr, nc = r + dr[x], c + dc[x]
                dfs(nr,nc,d+1, cnt+1)
                
        else:
            nr, nc = r + dr[d+1], c + dc[d+1]
            dfs(nr,nc,d+1, cnt+1)
        
            

dfs(0,0,0,1)
pprint(arr)
x = 1
for i in range(5):
    for j in range(5):
        arr[i][j] = x
        x=x+1
pprint(arr)