import sys
sys.stdin = open('c.txt', 'r')

def find(a, b):
    if b == 11:
        return

tc = int(input())
for sample in range(tc):
    arr = [list(map(int,input().split())) for _ in range(11)]
    