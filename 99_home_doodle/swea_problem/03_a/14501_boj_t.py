import sys; sys.stdin = open('t.txt', 'r')

def dfs(s):
    work[s] = 1
    m = []
    cnt = 0
    stack.append([s, info[s][0]])
    while stack:
        print(stack)
        check = len(stack)
        cnt += 1
        a = stack.pop()
        m.append(info[a[0]][1])
        print('money', m)
        for i in range(a[0]+a[1],n+1):
            if i+info[i][0] <= n+1:
                work[i] = 1
                stack.append([i, info[i][0]])

    

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.insert(0, 0)
stack = []
ma = 0

for i in range(1, n+1):
    if i+info[i][0] <= n+1:
        work = [0]*(n+1)
        dfs(i)
        