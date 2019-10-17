import sys; sys.stdin = open('ro.txt', 'r')

def clean(r, c, d, cnt, e):
    dr = (-1, 0, 1, 0)
    dc = (0, 1, 0, -1)
    if e == 4:
        nr, nc = r-dr[d%4], c-dc[d%4] # back
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc]:
                print(cnt)
                return
            else:
                clean(nr, nc, d, cnt, 0)
                return
        else:
            print(cnt)
            return
    visit[r][c] = True
    d-=1
    n = d%4
    nr = r+dr[n]; nc = c+dc[n]
    if not(0<=nr<N and 0<=nc<M):
        clean(r, c, d,cnt, e+1)
    else:
        if not visit[nr][nc] and not arr[nr][nc]:
            clean(nr, nc, d, cnt+1, 0)
        else:
            clean(r, c, d,cnt, e+1)
N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[False]*M for _ in range(N)]
clean(R, C, D, 1,0)