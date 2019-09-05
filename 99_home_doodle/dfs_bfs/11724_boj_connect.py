import sys; sys.stdin = open('c.txt', 'r')

def find(a):
    visit[a] = True
    for w in g[a]:
        if not visit[w]:
            find(w)
                
n, m = map(int, input().split())
cnt = 0
g = [[] for _ in range(n+1)]
visit = [False]*(n+1)
for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)
    g[v].append(u)
for i in range(1, n+1):
    if not visit[i]:
        cnt += 1
        find(i)
else:
    if False not in visit[1:]:
        print(cnt)
        
