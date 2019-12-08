import sys; sys.stdin = open('p.txt', 'r')

N, M, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
spin = [list(map(int, input().split())) for _ in range(T)]

for i in range(N):
    for idx, j in enumerate(arr[i]):
        arr[i][idx] = [j, idx, 1]
        if idx>0 and arr[i][idx][0]==arr[i][idx-1][0]:
            arr[i][idx][2], arr[i][idx-1][2] = 0, 0    
        if idx==M-1 and arr[i][0][0]==arr[i][-1][0]:
            arr[i][0][2], arr[i][-1][2] = 0, 0

for i in range(T):
    for j in range(N):
        # 반지름 지정
        if (j+1) % spin[i][0]: continue
        for c in range(spin[i][2]):
            if spin[i][1]:
                #반시계
                for k in range(M):
                    arr[j][k][1] -= 1
            else:
                # 시계
                for k in range(M):
                    arr[j][k][1] += 1
        for k in range(M):
            arr[j][k][1] = arr[j][k][1]%M
        # sorted(arr[j], key=lambda arr: arr[1])

for i in range(N-1):
    for j in range(M):
        for k in range(M):
            if arr[i][j][1] == arr[i+1][k][1] and arr[i][j][0]==arr[i+1][k][0]:
                arr[i][j][2], arr[i+1][k][2] = 0, 0
print(arr)
        