import sys
sys.stdin = open('1.txt', 'r')

tc = int(input())
for sample in range(tc):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    m = 99999
    for h in range(5, 0, -1):
        for i in range(n):
            cost_r = 0
            for idx in range(n):
                cost_r += abs(h-arr[i][idx])
            for j in range(n):
                cost_c = 0
                for jdx in range(n):
                    cost_c += abs(h-arr[jdx][j])
                cost_c -= abs(h-arr[i][j])
                if m >= cost_c+cost_r:
                    m = cost_c+cost_r
                    he = h
    print('#{} {} {}'.format(sample+1, m, he))