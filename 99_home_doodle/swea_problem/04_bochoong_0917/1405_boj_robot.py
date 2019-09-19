import sys
sys.stdin = open('c.txt','r')

tc = int(input())
for sample in range(tc):
    N = int(input())
    e, w, s, n = map(int, input().split())
    
