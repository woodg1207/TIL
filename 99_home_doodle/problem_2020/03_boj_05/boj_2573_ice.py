import sys; sys.stdin = open('i.txt', 'r')

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

print(arr)