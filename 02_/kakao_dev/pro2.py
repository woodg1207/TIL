import sys; sys.stdin = open('2.txt','r')

n, m = map(int, input().split())

for i in range(m):
    print('*'*n)