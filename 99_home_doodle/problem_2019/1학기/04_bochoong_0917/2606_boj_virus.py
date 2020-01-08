import sys
sys.stdin = open('v.txt', 'r')

def dfs(a):
    visit[a]=True
    for i in range(len(g[a])):
        if not visit[g[a][i]]:
            dfs(g[a][i])
v = int(input())
e = int(input())
arr = [list(map(int, input().split())) for _ in range(e)]
g = [[] for _ in range(v+1)]
visit = [False for _ in range(v+1)]
for i in arr:
    g[i[0]].append(i[1])
    g[i[1]].append(i[0])
dfs(1)
print(visit.count(True)-1)