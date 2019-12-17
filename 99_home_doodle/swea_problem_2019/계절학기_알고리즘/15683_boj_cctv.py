import sys; sys.stdin = open('cc.txt', 'r')

def cctvdir():
    
    return

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
cctv = []
cctv_dir = []
office = N*M
for i in range(N):
    for j in range(M):
        if 0<arr[i][j]<=5:
            cctv.append((i, j, arr[i][j]))
            if arr[i][j] == 2:
                cctv_dir.append(2)
            elif arr[i][j] == 5:
                cctv_dir.append(1)
            else: #1, 3, 4
                cctv_dir.append(4)
        elif arr[i][j] == 6:
            office -= 1
office -= len(cctv)
for i in range(len(cctv)):
    d = cctv_dir[i]
    while d:
        d-=1
        