import sys
sys.stdin = open('treasure.txt', 'r')
from pprint import pprint

from collections import deque
def bfs(a, b, c):
    global m
    da = [0, 1, 0, -1]
    db = [1, 0, -1, 0]
    q = deque()
    q.append([a, b])
    cnt = -1
    while q:
        cnt += 1
        for _ in range(len(q)):
            n = q.popleft()
            if visit[n[0]][n[1]]==c:continue
            visit[n[0]][n[1]] = c
            for i in range(4):
                nr = n[0] + da[i]
                nc = n[1] + db[i]
                if 0<=nr<N and arr[nr][n[1]] == 'L':
                    if visit[nr][n[1]]!=c:
                        q.append([nr, n[1]])
                if 0<=nc<M and arr[n[0]][nc] == 'L':
                    if visit[n[0]][nc]!=c:
                        q.append([n[0], nc])
    l.append(cnt)
    if m<cnt:
        m = cnt

N, M = map(int,input().split())
arr = [[i for i in input()] for _ in range(N)]
m = 0
l = []
x = 1
visit = [[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'W': continue
        bfs(i, j, x)
        x+=1
print(m)
print(l)