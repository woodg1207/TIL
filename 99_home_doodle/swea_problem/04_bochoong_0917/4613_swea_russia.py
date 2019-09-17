import sys
sys.stdin = open('r.txt', 'r')

tc = int(input())
for sample in range(tc):
    n, m = map(int, input().split())
    arr = [input() for _ in range(n)]
    