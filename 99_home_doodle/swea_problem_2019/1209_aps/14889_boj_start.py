import sys; sys.stdin = open('s.txt', 'r')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]

def build(s, cnt):
    global m
    if cnt == N/2:
        A, B = [], []
        for i in range(N):
            if v[i]:
                A.append(i)
            else:
                B.append(i)
        sa = sb = 0
        for i in range(len(A)):
            for j in range(i, len(A)):
                sa += arr[A[i]][A[j]] + arr[A[j]][A[i]]
                sb += arr[B[i]][B[j]] + arr[B[j]][B[i]]
        re = abs(sa-sb)
        if re == 0:
            m = 0
            return
        elif re<m:
            m = re

    for i in range(s, N):
        if v[i]:continue
        # l.append(i)
        v[i] = True
        build(i, cnt+1)
        # l.pop()
        v[i] = False
m = 100000
v = [False] * N
v[0] = True
build(0,1)
print(m)
