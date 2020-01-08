import sys
sys.stdin = open('m.txt', 'r')

# def dfs(a, b):
#     global re
#     visit.append([a, b])
#     print(visit)
#     if arr[a][b] == 3:
#         re = 1
#         return
#     if a+1<n  and arr[a+1][b]!=1 and [a+1, b] not in visit:
#         dfs(a+1,b)
#     if b+1<n and arr[a][b+1]!=1 and [a, b+1] not in visit:
#         dfs(a, b+1)
#     if 0<=a-1 and arr[a-1][b]!=1 and [a-1, b] not in visit:
#         dfs(a-1, b)
#     if 0<=b-1 and arr[a][b-1]!=1 and [a, b-1] not in visit:
#         dfs(a, b-1)

def dfs(a, b):
    global re
    # print(a, b)
    if arr[a][b] == 3:
        re = 1
        return
    arr[a][b] = 1
    if a+1<n and arr[a+1][b]!=1:
        dfs(a+1,b)
    if b+1<n and arr[a][b+1]!=1:
        dfs(a, b+1)
    if 0<=a-1 and arr[a-1][b]!=1:
        dfs(a-1, b)
    if 0<=b-1 and arr[a][b-1]!=1:
        dfs(a, b-1)

tc = int(input())
for sample in range(tc):
    n = int(input())
    arr = [[int(i) for i in input()] for _ in range(n)]
    visit = []
    re = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                arr[i][j] = 1
                dfs(i, j)
                break
    print('#{} {}'.format(sample+1, re))