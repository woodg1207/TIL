import sys; sys.stdin = open('c.txt', 'r')

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range()]