import sys; sys.stdin = open('g.txt', 'r')

N = int(input())
arr = list(map(int, input().split()))
info = [list(map(int, input().split())) for _ in range(N)]
for i in range(len(info)):
