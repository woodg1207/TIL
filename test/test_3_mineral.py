import sys
sys.stdin = open('m.txt', 'r')


def find(idx, a, b):
    global mineral
    if idx == len(m):
        return
    if a == 0:
        # print(l)
        if mineral < b:
            # print(l)
            mineral = b
        return
    if a < 0:
        return
    for i in range(idx+1, len(f)):
        # if i in l: continue
        l.append(i)
        find(i,a-(f[i]*2), b+arr[m[i][0]][m[i][1]])
        l.pop()

tc = int(input())
for sample in range(tc):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    m=[]
    l = []
    mineral = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and arr[i][j] != 1:
                m.append([i, j])
            if arr[i][j] == 1:
                robot = [i, j]
    # print(m)
    f = []
    for i in range(len(m)):
        x = abs(m[i][0]-robot[0])+abs(m[i][1]-robot[1])
        f.append(x)
    find(-1, C, 0)
    print('#{} {}'.format(sample+1, mineral))