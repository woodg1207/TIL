import sys
sys.stdin = open('m5.txt', 'r')

def find(a, b):
    if b == m :
        for i in l:
            print(arr[i], end=' ')
        print()
        return
    for i in range(n):
        if i in l: continue
        l.append(i)
        find(i, b+1)
        l.pop()

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
for i in range(n):
    l = []
    l.append(i)
    find(i, 1)