import sys
sys.stdin = open('t.txt', 'r')

from collections import deque
def bfs(a):
    q = [[]*len(a)]
    da = [0, 1, 0, -1]
    db = [1, 0, -1, 0]
    for i in range(len(a)):
        q[i].append(t[i])
        





M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
t = []
for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            t.append([i, j])
bfs(t)
