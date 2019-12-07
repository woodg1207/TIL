import sys; sys.stdin=open('n1.txt', 'r')

def perm(a, b):
    if b == M:
        print(*l)
        return
    for i in range(1, N+1):
        if v[i]: continue
        l.append(i)
        v[i] = True
        perm(i, b+1)
        l.pop()
        v[i] = False

N, M = map(int, input().split())
for i in range(1, N+1):
    v = [False] * (N+1)
    l = []
    l.append(i)
    v[i] = True
    perm(i, 1)