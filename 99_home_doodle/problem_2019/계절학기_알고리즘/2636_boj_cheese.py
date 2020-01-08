import sys; sys.stdin = open('c.txt', 'r')

from collections import deque

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
def bfs(r, c, hour):
    q = deque()
    q.append((r, c))



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
for i in range(1, N-1):
    for j in range(1, M-1):
        if arr[i][j] == 1:
            bfs(i, j, 0)