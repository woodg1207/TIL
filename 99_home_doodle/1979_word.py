import sys
sys.stdin = open('text_1979.txt')

testcase = int(input())
for sample in range(testcase):
    n, k = list(map(int, input().split()))
    box = [list(map(int, input().split())) for i in range(n)]
    cnt = 0
    for i in range(n):
        cnt_r = 0
        cnt_c = 0
        for j in range(n):
            if box[i][j] == 1:
                cnt_r += 1
            elif box[i][j] == 0: 
                if cnt_r == k:
                    cnt += 1
                    cnt_r = 0
                else:
                    cnt_r = 0
            if j == n-1 and cnt_r == k:
                cnt += 1
            if box[j][i] == 1:
                cnt_c += 1
            elif box[j][i] == 0:
                if cnt_c == k:
                    cnt += 1
                    cnt_c = 0
                else:
                    cnt_c = 0
            if j == n-1 and cnt_c ==k:
                cnt += 1
    print('#{} {}'.format(sample+1, cnt))

    #  row.append(box[i][j])
    #         column.append(box[j][i])
    #     for idx in range(n-k+1):
    #         if [1]*k == row[idx:idx+k] and row.count(1) == k:
    #             cnt += 1
    #         if [1]*k == column[idx:idx+k] and column.count(1) == k:
    #             cnt += 1
    #     else:
    #         row.clear()
    #         column.clear()