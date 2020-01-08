import sys; sys.stdin = open('cc.txt', 'r')


def blind_spot(x):
    for i in range(len(x)):
        if cctv[i][3] == 1:
            pass
        elif cctv[i][3] == 2:
            pass
        elif cctv[i][3] == 3:
            pass
        elif cctv[i][3] == 4:
            pass
        else:
            pass


def cctv_dir(cnt):
    if cnt == len(cctv):
        print(d_cctv)
        blind_spot(d_cctv)
        return
    for i in range(cctv[cnt][2]):
        d_cctv[cnt]=i
        cctv_dir(cnt + 1)



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
            cctv.append((i, j, d, arr[i][j]))
        elif arr[i][j] == 6:
            office -= 1
d_cctv = [-1]*(len(cctv))
cctv_dir(0)
office -= len(cctv)

