import sys
sys.stdin = open('l.txt', 'r')

def dfs(a,b):
    arr[a][b] = 0
    flag = 1
    if a==0:
        print('#{} {}'.format(sample, b))
        return 
    if b-1>=0 and arr[a][b-1]==1:
        flag = 0
        dfs(a,b-1)
    if b+1<100 and arr[a][b+1]==1:
        flag = 0
        dfs(a,b+1)
    if arr[a-1][b]==1 and flag:
        dfs(a-1,b)

for _ in range(10):
    sample = int(input())
    arr = [list(map(int,input().split())) for i in range(100)]
    for i in range(100):
        if arr[-1][i] == 2:
            dfs(99,i)
            break