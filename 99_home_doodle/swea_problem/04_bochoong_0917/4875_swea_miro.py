import sys
sys.stdin = open('m.txt', 'r')

tc = int(input())
for sample in range(tc):
    n = int(input())
    arr = [[int(i) for i in input()] for _ in range(n)]
    