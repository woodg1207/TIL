import sys; sys.stdin = open('s.txt', 'r')


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
player = [i for i in range(N)]


