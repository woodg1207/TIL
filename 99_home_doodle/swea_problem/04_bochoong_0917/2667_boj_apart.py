import sys
from pprint import pprint
sys.stdin = open('a.txt', 'r')


def dfs(a, b):
    global m, x
    arr[a][b]=0
    if a+1<n and arr[a+1][b]==1:
        x+=1
        dfs(a+1,b)
    if a-1>=0 and arr[a-1][b]==1:
        x += 1
        dfs(a-1,b)
    if b+1<n and arr[a][b+1]==1:
        x += 1
        dfs(a,b+1)
    if b-1>=0 and arr[a][b-1]==1:
        x += 1
        dfs(a,b-1)

n = int(input())
arr = [[int(i) for i in input()] for _ in range(n)]
cnt = 0
l = []
for i in range(n):
    for j in range(n):
        if arr[i][j]==1:
            cnt += 1
            x = 1
            dfs(i, j)
            l.append(x)
print(cnt)
l.sort()
for i in range(cnt):
    print(l[i])