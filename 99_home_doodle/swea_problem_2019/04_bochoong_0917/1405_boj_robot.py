import sys
from pprint import pprint
sys.stdin = open('c.txt','r')

def dfs(r, c, p, a):
    global k
    if arr[r][c]==1:
        k += p
        return
    if a == N:
        return
    if e:
        arr[r][c] = 1
        dfs(r,c+1,p*e,a+1)
        arr[r][c] = 0
    if w:
        arr[r][c] = 1
        dfs(r,c-1,p*w,a+1)
        arr[r][c] = 0
    if s:
        arr[r][c] = 1
        dfs(r+1,c,p*s,a+1)
        arr[r][c] = 0
    if n:
        arr[r][c] = 1
        dfs(r-1,c,p*n,a+1)
        arr[r][c] = 0

tc = int(input())
for sample in range(tc):
    N = int(input())
    e, w, s, n = map(int, input().split())
    e, w, s, n = e/100, w/100, s/100, n/100
    arr = [[0 for _ in range(29)] for _ in range(29)]
    cnt = 0
    k = 0
    dfs(14, 14, 1, cnt)
    print('{:.10f}'.format(1-k))
