import sys; sys.stdin = open('nm1.txt','r')

def nm(num, cnt):
    global result
    if cnt == M:
        print(*result)
        return
    for i in range(1, N+1):
        if visit[i]: continue
        result.append(i)
        visit[i] = True
        nm(i,cnt + 1)
        visit[i] = False
        result.pop()

N, M = map(int, input().split())
for i in range(1, N+1):
    visit = [False]*(N+1)
    result = [i]
    visit[i] = True
    nm(i, 1)