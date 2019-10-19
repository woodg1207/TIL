import sys; sys.stdin = open('z.txt', 'r')

import sys
sys.setrecursionlimit(10**6)
from collections import deque
dr = (1, 0, -1, 0)
dc = (0, -1, 0, 1)
def find(r,c,x):
    q = deque()
    visit[r][c] = x
    q.append((r,c))
    while q:
        a, b = q.popleft()
        visit[a][b] = x
        for idx in range(4):
            nr, nc = a+dr[idx], b+dc[idx]
            if 0<=nr<N and 0<=nc<N:
                if visit[nr][nc]==x: continue
                if arr[nr][nc]-x>0:
                    q.append((nr,nc))

 
N = int(input())
arr = [list(map(int,input().split())) for _ in range(N)]
M = 0
visit = [[-1]*N for _ in range(N)]
for H in range(101):
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]==H:continue
            if arr[i][j]-H<=0: continue
            find(i, j, H)
            cnt +=1
    if cnt==0:
        break
    if M<cnt:
        M=cnt
print(M)