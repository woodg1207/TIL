import sys; sys.stdin = open('num.txt', 'r')

def dfs(r, c):
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    stack = []
    stack.append([r, c])
    arr[r][c] = 0
    c = 1
    while stack:
        nr = stack[-1][0]
        nc = stack.pop()[1]
        for idx in range(4):
            if nr+dr[idx]>=0 and nr+dr[idx]<n and nc+dc[idx]<n and nc+dc[idx]>=0:
                if arr[nr+dr[idx]][nc+dc[idx]]!=0:
                    c += 1
                    arr[nr+dr[idx]][nc+dc[idx]]=0
                    stack.append([nr+dr[idx], nc+dc[idx]])
    check.append(c)           

n = int(input())
arr = [[int(i) for i in input()] for _ in range(n)]
cnt = 0
check = []
for i in range(n):
    for j in range(n):
        if arr[i][j] != 0:
            dfs(i, j)
            cnt += 1
print(cnt)
check.sort()
for i in range(len(check)):
    print(check[i])