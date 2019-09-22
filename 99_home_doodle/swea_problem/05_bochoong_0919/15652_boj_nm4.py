import sys
sys.stdin = open('m3.txt', 'r')

def find(a, b):
    if b == m:
        for i in l:
            print(i, end=' ')
        print()
        return
    for i in range(a, n+1):
        l.append(i)
        find(i, b+1)    
        l.pop()

n, m = map(int, input().split())
for i in range(1, n+1):
    l = []
    l.append(i)
    find(i, 1)