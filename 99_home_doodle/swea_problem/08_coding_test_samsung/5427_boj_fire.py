import sys; sys.stdin = open('f.txt', 'r')

from collections import deque
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)
def find(r,c):
    return

tc = int(input())
for sample in range(tc):
    W, H = map(int, input().split())
    arr = [[i for i in input()] for _ in range(H)]
