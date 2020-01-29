import sys; sys.stdin = open('h.txt', 'r')

def dfs(n):
    visit[n] = True
    for i in range(len(G[n])):
        if G[n][i] == 0: continue
        if visit[G[n][i]]: continue
        dfs(G[n][i])
    return

from collections import deque
def bfs(x):
    q = deque()
    q.append(x)
    visit[x] = True
    while q:
        nx = q.popleft()
        print(G[nx])
        # if visit[G[nx][i]]: continue
        for i in range(len(G[nx])):
            if visit[G[nx][i]]: continue
            visit[G[nx][i]] = True
            q.append(G[nx][i])

N, M = map(int, input().split())
G = [[False]]*(N+1)
# print(G)
for i in range(M):
    a, b = map(int, input().split())
    # print(G[a][0])
    if G[b][0]:
        G[b].append(a)
    else:
        G[b] = [a]
    # print(a, b)
    # print(G)

visit = [False]*(N+1)    
result = []
for i in range(1, N+1):
    if visit[i]: continue
    
    # dfs(i)
    bfs(i)
    print(visit)
    result.append(i)
print(*result)