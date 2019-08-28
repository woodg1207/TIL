import sys; sys.stdin = open('test.txt','r')
from pprint import pprint

testcase = int(input())
for sample in range(testcase):
    n, m, k = map(int, input().split())
    paints = [list(map(int, input().split())) for _ in range(k)]
    arr = [[0]*m for _ in range(n)]
    s = [0]
    for paint in paints:
        if paint[4] not in s:
            s.append(paint[4])
        flag = 1
        for i in range(paint[2]-paint[0]+1):
            if not flag:
                break
            for j in range(paint[3]-paint[1]+1):
                if arr[paint[0]+i][paint[1]+j] > paint[4]:
                    flag = 0
                    break
        if flag:
            for i in range(paint[2] - paint[0] + 1):
                for j in range(paint[3] - paint[1] + 1):
                    arr[paint[0] + i][paint[1] + j] = paint[4]
    max_cnt = 0

    for color in s:
        cnt = 0
        for i in range(n):
            cnt += arr[i].count(color)

        if max_cnt < cnt:
            max_cnt = cnt


    print('#{} {}'.format(sample+1, max_cnt))



