import sys; sys.stdin = open('p.txt', 'r')

def find(r, c, dir):
    global cnt
    if r == N-1 and c == N-1:
        cnt += 1
        return
    l = 3
    if dir != 1:
        l = 2
    for i in range(l):
        if dir ==2:
            i += 1
        nr = r + dr[i]
        nc = c + dc[i]
        if 0<=nr<N and 0<=nc<N:
            if arr[nr][nc]: continue
            if i == 1:
                if arr[r+1][c]: continue
                elif arr[r][c+1]:continue
            if dir == 0:
                if i == 0:
                    if nc == N - 1 and nr != N - 1: continue
            elif dir == 1:
                if i == 0:
                    if nc == N - 1 and nr != N - 1: continue
                elif i ==2:
                    if nr == N - 1 and nc != N - 1: continue
            elif dir == 2:
                if i ==2:
                    if nr == N - 1 and nc != N - 1: continue
            find(nr, nc, i)



import time
start = time.time()  # 시작 시간 저장

dr = (0, 1, 1)
dc = (1, 1, 0)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
memo = [[False]*N for _ in range(N)]
find(0, 1, 0)
print(cnt)

print("time :", time.time() - start)

