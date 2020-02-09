import sys; sys.stdin = open('l.txt', 'r')
from pprint import pprint

from collections import deque
dr = [1, 0, -1, 0]
dc = [0, -1, 0, 1]
def bfs(vi):
    q = deque()
    cnt = 0
    visit = [[False]*N for _ in range(N)]
    for i in vi:
        q.append(i)
    while q:
        x = len(q)
        for j in range(len(q)):
            nr, nc = q.popleft()
            visit[nr][nc] = True
            for i in range(4):
                nr, nc = nr + dr[i], nc + dc[i]
                if 0<=nr<N and 0<=nc<N:
                    if visit[nr][nc]: continue
                    if lab[nr][nc]==1:continue 
                    # if lab[nr][nc]==2:
                    q.append((nr, nc))
        cnt += 1
    return cnt


def comb(a, depth):
    global Min
    if depth == M:
        re = bfs(v_position)
        if Min > re:
            Min = re
        return
    for i in range(a+1, len(virus)):
        v_position.append(virus[i])
        comb(i,depth+1)
        v_position.pop()

N, M  = map(int, input().split())
lab = [list(map(int, input().split())) for _ in range(N)]
virus = []
Min = N*N
for i in range(N):
    for j in range(N):
        if lab[i][j] == 2:
            virus.append((i, j))
for i in range(len(virus)-M+1):
    v_position = [virus[i]]
    comb(i,1)
print(Min)