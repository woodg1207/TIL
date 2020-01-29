import sys; sys.stdin = open('nm2.txt', 'r')

def nm(num, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(1, N+1):
        result.append(i)       
        nm(i,cnt + 1)
        result.pop()

N, M = map(int, input().split())
for i in range(1, N+1):
    result = [i]
    nm(i, 1)