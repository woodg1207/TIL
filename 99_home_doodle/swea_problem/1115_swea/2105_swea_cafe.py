import sys; sys.stdin = open('cafe.txt', 'r')

def findcafe(a, b):
    global M
    p1 = []
    p2 = []
    for i in range(a+1, N):
        for j in range(N):
            if a+b == i+j:
                p1.append((i, j))
            if a-b == i-j:
                p2.append((i, j))
    for idx in range(len(p1)):
        for jdx in range(len(p2)):
            if p1[idx][0] > p2[jdx][0]:
                x = p1[idx][0]
            else:
                x = p2[jdx][0]
            p3 = False
            for i in range(x+1, N):
                for j in range(p1[idx][1]+1, p2[jdx][1]):
                    if i+j == p2[jdx][0]+p2[jdx][1] and i-j == p1[idx][0]-p1[idx][1]:
                        p3 = (i, j)
            if p3:
                flag = 0
                cafe = [False] * 101
                cafe[arr[a][b]] = True
                # p1 판별
                for i in range(a+1, p1[idx][0] + 1):
                    j = a + b - i
                    if cafe[arr[i][j]]:
                        flag = 1
                        break
                    else:
                        cafe[arr[i][j]] = True
                if flag: continue
                # p2 판별
                for i in range(a+1, p2[jdx][0]+1):
                    j = i-a+b
                    if cafe[arr[i][j]]:
                        flag = 1
                        break
                    else:
                        cafe[arr[i][j]] = True
                if flag: continue
                # p3 판별
                for i in range(p1[idx][0]+1, p3[0]+1):
                    j = i - p1[idx][0]+p1[idx][1]
                    if cafe[arr[i][j]]:
                        flag = 1
                        break
                    else:
                        cafe[arr[i][j]] = True
                if flag: continue
                for i in range(p2[jdx][0]+1, p3[0]):
                    j = p2[jdx][0]+p2[jdx][1] - i
                    if cafe[arr[i][j]]:
                        flag = 1
                        break
                    else:
                        cafe[arr[i][j]] = True
                if flag: continue
                ###
                if M < cafe.count(True):
                    M = cafe.count(True)

tc = int(input())
for sample in range(tc):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    M = 0
    for i in range(N-2):
        for j in range(1,N-1):
            findcafe(i, j)
    if M == 0:
        M = -1
    print('#{} {}'.format(sample+1, M))
