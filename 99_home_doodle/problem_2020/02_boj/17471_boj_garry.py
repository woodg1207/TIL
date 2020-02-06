import sys; sys.stdin = open('g.txt', 'r')


from collections import deque
def bfs(num, lists):
    q=deque()
    v=[False]*(N+1)
    q.append(num)
    v[num] = True
    while q:
        next_num = q.popleft()
        for i in range(len(G[next_num])):
            if v[G[next_num][i]]: continue
            if G[next_num][i] in lists:
                v[G[next_num][i]] = True
                q.append(G[next_num][i])
    return v.count(True)

def comb(a):
    global l, result
    flag = 0
    for i in range(a+1, N+1):
        l.append(i)
        visit[i] =True
        comb(i)
        l.pop()
        visit[i] = False
    if len(l)==N:
        return
    notl = []
    for i in range(1, N+1):
        if not visit[i]:
            notl.append(i)    
    if len(l) != bfs(l[0],l) or len(notl) != bfs(notl[0],notl):return
    sum_a, sum_b = 0, 0 
    for i in l:
        sum_a += people[i-1]
    for i in notl:
        sum_b += people[i-1]   
    re = abs(sum_a-sum_b)
    if result>re:
        result = re
    return

result = 0xffff
N = int(input())
people = list(map(int, input().split()))
G = [[False]]
for i in range(1, N+1):
    a = list(map(int, input().split()))
    G.append(a[1:])
visit = [False] *(N+1)
l = [1]
visit[1] = True
comb(1)
if result!=0xffff:
    print(result)
else:
    print(-1)