import sys
sys.stdin = open('pass.txt', 'r')

def find(a, b):
    if b == L:
        cnt = 0
        for i in range(L):
            if arr[l[i]] in beta:
                cnt += 1
            if cnt>L-2:
                return
        if cnt==0:
            return
        for i in range(L):
            print(arr[l[i]], end='')
        print()
        return
    for i in range(a+1,C):
        l.append(i)
        find(i, b+1)
        l.pop()

L, C = map(int, input().split())
arr = input().split()
beta = 'aeiou'
arr.sort()
for i in range(C):
    if arr[i] in beta:
        stop=i
for i in range(stop+1):
    l = []
    l.append(i)
    find(i, 1)
