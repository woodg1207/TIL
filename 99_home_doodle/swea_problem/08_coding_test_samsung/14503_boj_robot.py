import sys; sys.stdin = open('ro.txt', 'r')

N, M = map(int, input().split())
R, C, D = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
