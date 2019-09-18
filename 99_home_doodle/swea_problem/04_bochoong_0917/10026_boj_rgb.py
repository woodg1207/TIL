import sys
sys.stdin = open('rgb.txt', 'r')
from pprint import pprint
import sys, copy
sys.setrecursionlimit(10**6)

def dfs(a, b, c):
    arr[a][b] = 'a'
    if a-1>=0 and arr[a-1][b] in c:
        dfs(a-1, b, c)
    if a+1<n and arr[a+1][b] in c:
        dfs(a+1, b, c)
    if b-1>=0 and arr[a][b-1] in c:
        dfs(a, b-1, c)
    if b+1<n and arr[a][b+1] in c:
        dfs(a, b+1, c)

n = int(input())
arr = [[i for i in input()] for _ in range(n)]
cnt = 0
cnt_m = 0
arrr = copy.deepcopy(arr)
for i in range(n):
    for j in range(n):
        if arr[i][j] != 'a':
            if arr[i][j] == 'B':
                dfs(i, j, 'B')
            else: 
                dfs(i, j, 'GR')
            cnt += 1
arr = arrr
for i in range(n):
    for j in range(n):
        if arr[i][j] != 'a':
            if arr[i][j] == 'B':
                dfs(i,j,'B')
            elif arr[i][j] == 'G':
                dfs(i,j,'G')
            else:
                dfs(i,j,'R')
            cnt_m += 1
print(cnt_m, cnt)