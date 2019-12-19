import sys; sys.stdin = open('f.txt', 'r')

from collections import deque
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
def find(x):
    q = deque()
    for i in range(len(x)):
        q.append(x[i])
        if x[i][2]==1:
            visit[x[i][0]][x[i][1]] = 1
        if x[i][2]==2:
            visit[x[i][0]][x[i][1]] = 2
    while q:
        n = q.popleft()
        # print(n)
        if n[2]==1 and ((n[0]==0 or n[0]==H-1) or (n[1]==0 or n[1]==W-1)):
            print(n[3])
            return
        if n[2]==1:
            visit[n[0]][n[1]] = 1
        elif n[2]==2:
            visit[n[0]][n[1]] = 2
        for idx in range(4):
            nr, nc = n[0]+dr[idx], n[1]+dc[idx]
            if 0<=nr<H and 0<=nc<W:
                if visit[nr][nc] > n[2]: continue
                if n[2]==1:
                    if 0<=nr+dr[idx]<H and 0<=nc+dc[idx]<W: 
                        if visit[nr+dr[idx]][nc+dc[idx]] == 2: continue
                if arr[nr][nc]=='.':
                    q.append((nr, nc, n[2], n[3]+1))
    print('IMPOSSIBLE')

tc = int(input())
for sample in range(3):
    W, H = map(int, input().split())
    arr = [0]*H
    visit = [[0]*W for _ in range(H)]
    a = []
    for i in range(H):
        arr[i]=input()
        for j in range(W):
            if arr[i][j]=='@':
                a.append([i, j, 1, 1])
            if arr[i][j]=='*':
                a.append([i, j, 2, 1])
    find(a)