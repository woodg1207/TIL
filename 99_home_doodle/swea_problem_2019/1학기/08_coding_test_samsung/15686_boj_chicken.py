import sys; sys.stdin = open('c.txt', 'r')

def comb(a, b):
    global result
    if b == M:
        H = [0xffff]*(len(h))
        for i in range(len(l)):
            for j in range(len(h)):
                d = abs(l[i][0]-h[j][0])+abs(l[i][1]-h[j][1])
                if H[j] > d:
                    H[j] = d
        if result>sum(H):
            result = sum(H)
        return
    for i in range(a+1, len(c)):
        l.append(c[i])
        comb(i, b+1)
        l.pop()

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
c, h = [], []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            h.append([i, j])
        elif arr[i][j] == 2:
            c.append([i, j])
result = 0xfffff
for i in range(len(c)):
    l = []
    l.append(c[i])
    comb(i, 1)
print(result)