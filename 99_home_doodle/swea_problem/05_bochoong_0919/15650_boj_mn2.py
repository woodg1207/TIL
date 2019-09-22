import sys
sys.stdin = open('m2.txt', 'r')

def comb(a, b):
    if b == m:
        for i in l:
            print(i, end=' ')
        print()
        return
    for i in range(a,n+1):
        if i not in l:
            l.append(i)
            comb(i+1, b+1)
            l.pop()

n, m = map(int, input().split())
for i in range(1, n+1):
    l = []
    l.append(i)
    comb(i, 1)    
