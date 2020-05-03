import sys; sys.stdin = open('2636.txt','r')
from collections import deque

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

day = 0
cnt = 0
memory = []
while 1:
    day += 1
    visit = [[False]*M for _ in range(N)]
    q = deque()
    q.append((0,0))
    visit[0][0]=True
    l = []
    while q:
        n = q.popleft()
        for i in range(4):
            nr, nc = n[0]+dr[i], n[1]+dc[i]
            if 0<=nr<N and 0<=nc<M:
                if visit[nr][nc]: continue
                if arr[nr][nc]==0:
                    visit[nr][nc] = True
                    q.append((nr,nc))
                else:
                    # if visit[nr][nc]: continue
                    visit[nr][nc]=True
                    arr[nr][nc]=0
                    l.append((nr, nc))
    if not len(l):
        print(day-1)
        print(len(memory.pop()))
        break
    memory.append(l)


    