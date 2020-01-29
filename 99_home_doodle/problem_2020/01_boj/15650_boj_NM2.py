import sys; sys.stdin = open('nm2.txt', 'r')

N, M = map(int, input().split())
def find(num, cnt):
    if cnt == M:
        print(*result)
        return
    for i in range(num, N+1):
        result.append(i)
        find(i, cnt+1)
        result.pop()

for i in range(1, N+1):
    result = [i]
    find(i, 1)
        