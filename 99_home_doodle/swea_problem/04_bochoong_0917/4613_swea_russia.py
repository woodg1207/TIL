from pprint import pprint
import sys
sys.stdin = open('r.txt', 'r')

tc = int(input())
for sample in range(tc):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    mini = 99999
    for i in range(1, n-1):
        for j in range(1, n-i):
            a,b,c = 0,0,0
            for idx in range(i):
                # print(idx,'www')
                a += arr[idx].count('W')
            for jdx in range(i,j+i):
                # print(jdx,'bbb')
                b += arr[jdx].count('B')
            for kdx in range(i+j, n):
                # print(kdx,'rrr')
                c += arr[kdx].count('R')
            # print(i,j,m*n-a-b-c)
            if mini > m*n-a-b-c:
                mini = m*n - a - b - c
    print('#{} {}'.format(sample+1, mini))