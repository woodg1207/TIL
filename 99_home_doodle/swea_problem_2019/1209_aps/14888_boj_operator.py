import sys; sys.stdin = open('o.txt', 'r')

def operator(r, idx, op):
    global m, M
    if op == 0:
        r += A[idx]
    elif op == 1:
        r -= A[idx]
    elif op == 2:
        r *= A[idx]
    else:
        if r<0:
            r = (-1)*(((-1)*r)//A[idx])
        else:
            r = r//A[idx]
    if idx == N-1:
        if r<m:
            m = r
        if r>M:
            M = r
        return
    for i in range(len(O)):
        if v[i]: continue
        v[i] =True
        operator(r, idx+1, O[i])
        v[i] = False

N = int(input())
A = list(map(int, input().split()))
o = list(map(int, input().split()))
O = []
for i in range(len(o)):
    if not o[i]:continue
    for j in range(o[i]):
        O.append(i)

m = 0xffffffff
M = m*(-1)
for i in range(len(O)):
    v = [False]*(N-1)
    v[i] = True
    operator(A[0], 1, O[i])
print(M); print(m)