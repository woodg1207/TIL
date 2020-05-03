import sys; sys.stdin = open('2667.txt', 'r')
from pprint import pprint
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]

dr = [1, 0, -1,0]
dc = [0, 1, 0,-1]
def dfs(r, c):
    global m
    arr[r][c] = 0
    
    for i in range(4):
        nr, nc = r + dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc] == 0: continue
            dfs(nr, nc)
            m += 1       

l = []
apt_cnt = 0
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            m = 1
            apt_cnt += 1
            dfs(i, j)
            l.append(m)

print(apt_cnt)
for i in sorted(l):
    print(i)