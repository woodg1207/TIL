import sys; sys.stdin = open('2468.txt','r')
import sys
sys.setrecursionlimit(10**6)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def dfs(r, c, h):
    global visit
    visit[r][c] = True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<N:
            if visit[nr][nc] or arr[nr][nc] <= h: continue
            dfs(nr, nc, h)
Max = 1
for water in range(101):
    visit = [[False]*N for _ in range(N)]
    cnt = 0    
    for i in range(N):
        for j in range(N):
            if visit[i][j] or arr[i][j] <= water: continue
            cnt += 1
            dfs(i, j, water)
    if Max < cnt:
        Max = cnt
        # print(water)
    if cnt == 0:
        # print(water)
        break
print(Max)
                