import sys; sys.stdin = open('s.txt', 'r')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]

def build(cnt):
    if cnt == N/2:
        A, B = [], []
        for i in range(N):
            if v[i]:
                A.append(i)
            else:
                B.append(i)
        synergy(A)
        return
    for i in range(N):
        if v[i]:continue
        l.append(i)
        v[i] = True
        build(cnt+1)
        l.pop()
        v[i] = False

def synergy(a):
    for i in range(len(a)):
        s = []
        s.append(a[i])
        for j in range(len(a)):
            

for i in range(N//2):
    l = []
    v = [False] * N
    l.append(i)
    v[i] = True
    build(1)
