import sys; sys.stdin = open('p.txt', 'r')

def find(r, c, dir):
    global cnt
    # print(r, c)
    if r == N-1 and c == N-1:
        cnt += 1
        branch = 1
        return branch
    l = 3
    if dir == 0 or dir == 2:
        l = 2
    count = 0
    for i in range(l):
        if dir ==2:
            i += 1
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N:
            if dir == 0 or dir == 1:
                if i == 0 and (nc == N - 1 and nr != N - 1): continue
            elif dir == 2 or dir == 1:
                if i == 2 and (nr == N - 1 and nc != N - 1): continue
            if arr[nr][nc]: continue
            if i == 1 and (arr[r+1][c] or arr[r][c+1]):continue
            count += 1
            find(nr, nc, i)



dr = (0, 1, 1)
dc = (1, 1, 0)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
memo = [[False]*N for _ in range(N)]
find(0, 1, 0)
print(cnt)



