import sys; sys.stdin = open('h.txt', 'r')

def dfs(n):
    visit[n] = True
    for i in range(len(G[n])):
        if G[n][i] == 0: continue
        if visit[G[n][i]]: continue
        dfs(G[n][i])

N, M = map(int, input().split())
G = [[]]*(N+1)
for i in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
    
visit = [False]*(N+1)    
result = []
for i in range(1, N+1):
    if visit[i]: continue
    dfs(i)
    result.append(i)
print(*result)