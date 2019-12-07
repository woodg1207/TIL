import sys; sys.stdin = open('n2.txt', 'r')

def con(a, b):
    if b == M:
        print(*l)
        return
    for i in range(a+1, N+1):
        l.append(i)
        con(i, b+1)
        l.pop()


N, M = map(int, input().split())
for i in range(1, N+1):
    l = []
    l.append(i)
    con(i, 1)