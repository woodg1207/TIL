import sys
sys.stdin = open('l.txt', 'r')
from pprint import pprint

from collections import deque
def bfs(a, b):
    da = [0, 1, 0, -1]
    db = [1, 0, -1, 0]
    cnt = 0
    q = deque()
    q.append([a, b])
    while q:
        n = q.popleft()
        if arr[n[0]][n[1]] == 1:
            continue
        arr[n[0]][n[1]] = 1
        cnt += 1
        for i in range(4):
            nr = n[0] + da[i]
            nc = n[1] + db[i]
            if 0<=nr<M and arr[nr][n[1]]==0:
                q.append([nr, n[1]])
            if 0<=nc<N and arr[n[0]][nc]==0:
                q.append([n[0], nc])
    l.append(cnt)

M, N, K = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(K)]
arr = [[0]*N for _ in range(M)]
for x in range(K):
    for i in range(M):
        for j in range(N):
            if info[x][0] <= j < info[x][2]:
                if info[x][1] <= i < info[x][3]:
                    arr[i][j] = 1
c = 0
l = []
for i in range(M):
    for j in range(N):
        if arr[i][j] == 1: continue
        bfs(i, j)
        c += 1
print(c)
l.sort()
for i in range(len(l)):
    print(l[i], end=' ')
print()