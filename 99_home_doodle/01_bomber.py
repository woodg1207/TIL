import sys
sys.stdin = open('samplebomber1.txt', 'r')

testcase = int(input())
for sample in range(testcase):
    n = int(input())
    arr = [list(map(int, input().split())) for i in range(n)]
    
    row = []
    column = []

    bomb_max = 0

    for i in range(n):
        cnt_r, cnt_c = 0, 0
        for j in range(n):
            cnt_c += arr[j][i]
            cnt_r += arr[i][j]
        row.append(cnt_r)
        column.append(cnt_c)
        cnt_c, cnt_r = 0, 0
    
    for i in range(n):
        for j in range(n):
            if bomb_max <= row[i]+column[j]-arr[i][j]:
                bomb_max = row[i]+column[j]-arr[i][j]
                r=i
                c=j
    print('#{} 행:{} 열:{} {}'.format(sample+1, r, c, bomb_max))