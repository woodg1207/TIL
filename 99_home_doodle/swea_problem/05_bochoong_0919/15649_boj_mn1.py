import sys
sys.stdin = open('m1.txt','r')

def perm(a, b):
    if b == m:
        for i in l:
            print(i, end=' ')
        print()
        return
    for i in range(1, n+1):
        if i in l:
            pass
        else:
            l.append(i)
            perm(i,b+1)
            l.pop()
      
n, m = map(int,input().split())
for i in range(1, n+1):
    l = []
    l.append(i)
    perm(i, 1)