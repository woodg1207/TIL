import sys
sys.stdin = open('c.txt', 'r')
from pprint import pprint



from queue import Queue
def bfs(a, b):
    da = [0, 1, 0, -1]
    db = [1, 0, -1, 0]
    arr[a][b] = 0
    q = Queue()
    q.put([a, b])
    while q.qsize():
        n = q.get()
        for i in range(4):
            na = n[0]+da[i]
            nb = n[1]+db[i]
            if 0<=na<N and 0<=nb<M:
                if arr[na][nb] == 1:
                    arr[na][nb] = 0
                    q.put([na, nb])

tc = int(input())
for sample in range(tc):
    M, N, K = map(int, input().split())
    info = [list(map(int, input().split())) for _ in range(K)]
    arr = [[0]*M for _ in range(N)]
    for c in range(K):
        for i in range(N):
            for j in range(M):
                if i == info[c][1] and j == info[c][0]:
                    arr[i][j] = 1
    cnt = 0
    for i in range(K):
        if arr[info[i][1]][info[i][0]] == 0: continue
        bfs(info[i][1], info[i][0])
        cnt += 1
    print(cnt)