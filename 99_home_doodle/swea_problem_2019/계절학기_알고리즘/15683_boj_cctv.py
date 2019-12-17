import sys; sys.stdin = open('cc.txt', 'r')

def cctv_dir(cctvd):
    
    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
cctv = []

office = N*M
for i in range(N):
    for j in range(M):
        if 0<arr[i][j]<=5:
            if arr[i][j] == 2:
                d = 2
            elif arr[i][j] == 5:
                d = 1
            else: #1, 3, 4
                d = 4
            cctv.append((i, j, d))
        elif arr[i][j] == 6:
            office -= 1
office -= len(cctv)
