import sys; sys.stdin = open('i.txt', 'r')
from pprint import pprint

from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
cnt = 0

def bfs(r, c):
    q = deque()
    q.append((r, c))
    while q:
        n = q.popleft()
        print(q)
        visit[n[0]][n[1]] = 1
        count = 0
        for i in range(4):
            nr = n[0] + dr[i]
            nc = n[1] + dc[i]
            if visit[nr][nc]: continue
            if arr[nr][nc] <= 0:
                count += 1
            else:
                q.append((nr, nc))


for i in range(N):
    for j in range(M):
        if arr[i][j] > 0:
            visit = [[0] * M for _ in range(N)]
            melt = [[0] * M for _ in range(N)]
            bfs(i, j)
            cnt += 1


