import sys; sys.stdin = open('p.txt', 'r')

import sys
sys.setrecursionlimit(10**6)
def find(r, c, dir):
    global cnt
    if r == N-1 and c == N-1:
        cnt += 1
        w = 1
        return w
    if memo[dir][r][c] != -1:
        return memo[dir][r][c]
    l = 3
    if dir != 1:
        l = 2
    w = 0
    for i in range(l):
        if dir == 2:
            i += 1
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
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
                elif i == 2:
                    if nr == N - 1 and nc != N - 1: continue
            elif dir == 2:
                if i == 2:
                    if nr == N - 1 and nc != N - 1: continue
            w += find(nr, nc, i)
    memo[dir][r][c] = w
    return w

import time
start = time.time()  # 시작 시간 저장

dr = (0, 1, 1)
dc = (1, 1, 0)
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt = 0
memo = [[[-1]*N for _ in range(N)] for _ in range(3)]
print(find(0, 1, 0))

print("time :", time.time() - start)