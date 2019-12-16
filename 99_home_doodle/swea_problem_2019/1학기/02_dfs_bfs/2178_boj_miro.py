import sys; sys.stdin = open('m.txt', 'r')
from pprint import pprint

def bfs(r, c):
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    q =[]
    q.append([r, c])
    arr[r][c] = 0
    cnt = 1
    while q:
        cnt += 1
        for _ in range(len(q)):
            r = q[0][0]
            c = q.pop(0)[1]
            for idx in range(len(dr)):
                if r+dr[idx]>=0 and r+dr[idx]<n and c+dc[idx]>=0 and c+dc[idx]<m:
                    if r+dr[idx]==n-1 and c+dc[idx]==m-1:
                        return cnt
                    elif arr[r+dr[idx]][c+dc[idx]]==1:
                        if [r+dr[idx], c+dc[idx]] not in q:
                            q.append([r+dr[idx], c+dc[idx]])
                        arr[r][c]=0
n, m = map(int, input().split())
arr = [[int(i) for i in input()] for _ in range(n)]
print(bfs(0,0))