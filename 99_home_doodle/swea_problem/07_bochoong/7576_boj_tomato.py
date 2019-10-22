import sys
from pprint import pprint
sys.stdin = open('t.txt', 'r')

from collections import deque
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
def bfs(a):
    q = deque()
    for i in a:
        q.append([i[0], i[1], 0])
    while q:
        n = q.popleft()
        if visit[n[0]][n[1]]: continue
        visit[n[0]][n[1]] = 1
        d = n[2]
        for i in range(4):
            nr = n[0] + dr[i]
            nc = n[1] + dc[i]
            if 0<=nr<N and 0<=nc<M:
                if visit[nr][nc]:continue
                q.append([nr, nc, n[2]+1])
    for i in range(N):
        if M != sum(visit[i]):
            print('-1')
            return
    print(d)

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t = []
visit = [0]*N
for i in range(N):
    visit[i] = [0]*M
    for j in range(M):
        if arr[i][j]==1:
            t.append([i, j])
        elif arr[i][j]==-1:
            visit[i][j] = 1
bfs(t)
