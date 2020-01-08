import sys; sys.stdin = open('o.txt', 'r')


from copy import deepcopy
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
    for i in range(4):
        if o[i]:
            o[i] -= 1
            operator(r, idx+1, i)
            o[i] += 1


N = int(input())
A = list(map(int, input().split()))
O = list(map(int, input().split()))
m = 0xffffffff
M = m*(-1)
for i in range(4):
    o = deepcopy(O)
    if o[i]:
        o[i] -= 1
        operator(A[0], 1, i)
print(M); print(m)