n, m = list(map(int, input().split())) #n 행 m 열 
chess = [list(input().split()) for i in range(n)]
# b = 1, w = 0 이진법으로 풀기 xor사용
for i in range(n):
    chess[i] = ''.join(chess[i]).replace('B', '1')
    chess[i] = ''.join(chess[i]).replace('W', '0')
## case 만들어주기
case1 = []
case2 = []
for i in range(4):
    case1.append('10101010')
    case1.append('01010101')
for i in range(4):
    case2.append('01010101')
    case2.append('10101010')
##체스 비교 
cnt_min1 = []
cnt_min2 = []
minnum=64
for i in range(n-8+1):
    for j in range(m-7):
        for idx in range(8):
            cnt = int(case1[idx], 2)^int(chess[i+idx][j:j+8], 2)
            cnt_min1.append(str(bin(cnt)).count('1'))
        if minnum > sum(cnt_min1):
            minnum = sum(cnt_min1)
        cnt_min1 = []
for i in range(n-8+1):
    for j in range(m-7):
        for idx in range(8):
            cnt = int(case2[idx], 2)^int(chess[i+idx][j:j+8], 2)
            cnt_min2.append(str(bin(cnt)).count('1'))
        if minnum > sum(cnt_min2):
            minnum = sum(cnt_min2)
        cnt_min2 = []
print(minnum)

