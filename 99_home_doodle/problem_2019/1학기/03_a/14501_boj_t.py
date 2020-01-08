import sys; sys.stdin = open('t.txt', 'r')

def dfs(s):
    global ma
    work[s] = 1
    m = []
    cnt = 0
    c= 0
    stack.append([s, info[s][0]])
    while stack:
        print(stack)
        # print('mm', m, sum(m), c)
        a = stack.pop()
        m.append(info[a[0]][1])
        print('ooooo', m, sum(m), c)
        flag = 1
        cnt += 1
        c = 0
        for i in range(a[0]+a[1], n+1):
            if i+info[i][0]<=n+1:
                stack.append([i,info[i][0]])
                flag = 0
                c += 1
        if a[0]+a[1] == n+1:
            cnt += 1
            m.append(info[a[0]][1])


        if flag:
            if ma < sum(m):
                ma = sum(m)
            for idx in range(cnt-1):
                cnt -= 1
                m.pop()



n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.insert(0, 0)
stack = []
ma = 0

for i in range(1, n+1):
    if i+info[i][0] <= n+1:
        work = [0]*(n+1)
        dfs(i)
        break


print(ma)

        