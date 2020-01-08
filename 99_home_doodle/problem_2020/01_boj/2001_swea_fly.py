import sys; sys.stdin=open('f.txt', 'r')
from pprint import pprint


testcase = int(input())
for sample in range(1, testcase+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    kill_max = 0
    for i in range(N-M+1):
        for j in range(N-M+1):
            result = 0
            for x in range(M):
                result += sum(arr[i+x][j:M+j])
            if result > kill_max:
                kill_max = result
    print('#{} {}'.format(sample, kill_max))