import sys; sys.stdin = open('r.txt', 'r')

tc = int(input())
for sample in range(tc):
    K = int(input())
    arr = [list(map(int,input().split())) for _ in range(4)]
    info = [list(map(int, input().split())) for _ in range(K)]
