import sys
sys.stdin = open('h.txt', 'r')


import sys
sys.setrecursionlimit(99999999)

from collections import deque
def bfs(a):
    visit[a] = True
    q = deque()
    q.append(a)
    while q:
        n = q.popleft()
        for i in range(len(G[n])):
            if visit[G[n][i]]:continue
            visit[G[n][i]] = True
            q.append(G[n][i])

def dfs(a):
    visit[a] = True
    for i in range(len(G[a])):
        if visit[G[a][i]]:continue
        dfs(G[a][i])

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(M)]
G = [[] for _ in range(N+1)]
visit = [False] * (N+1)
for i in range(M):
    G[arr[i][1]].append(arr[i][0])
# print(G)
for i in range(1, len(visit)):
    # print(i)
    if visit[i]: continue
    dfs(i)
    print(i,end=' ')
