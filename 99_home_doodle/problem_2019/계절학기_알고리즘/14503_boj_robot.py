import sys; sys.stdin = open('r.txt', 'r')
from pprint import pprint
dr = (-1, 0, 1, 0)
dc = (0, 1, 0, -1)
N, M = map(int, input().split())
robot = list(map(int, input().split()))
arr = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
def clean_r(r, c, d, cnt):
    visit[r][c] = 1
    for i in range(-3, 1):
        ndir = (d-i) % 4
        nr = r + dr[ndir]
        nc = c + dc[ndir]
        if 0<=nr<N and 0<=nc<M:
            if arr[nr][nc] or visit[nr][nc]: continue
            clean_r(nr, nc, ndir, cnt+1)
            return
    if arr[r-dr[d]][c-dc[d]]:
        print(cnt)
        return
    else:
        clean_r(r-dr[d], c-dc[d], d, cnt)
clean_r(robot[0], robot[1], robot[2], 1)