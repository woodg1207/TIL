import sys; sys.stdin = open('cc.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
cctv = []
office = N*M
for i in range(N):
    for j in range(M):
        if 0<arr[i][j]<=5:
            cctv.append((i, j, arr[i][j]))
        elif arr[i][j] == 6:
            office -= 1
office -= len(cctv)
