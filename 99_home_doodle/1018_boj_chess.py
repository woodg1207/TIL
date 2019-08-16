# n, m = list(map(int, input().split())) #n 행 m 열 
# chess = [list(input().split()) for i in range(n)]
# print(chess)
# # b = 1, w = 0 이진법으로 풀기 xor사용
# for i in range(n):
#     chess[i] = ''.join(chess[i]).replace('B', '1')
#     chess[i] = ''.join(chess[i]).replace('W', '0')
case1 = []
case2 = []
for i in range(4):
    case1.append('10101010')
    case1.append('01010101')
for i in range(4):
    
