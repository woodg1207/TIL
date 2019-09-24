import sys
sys.stdin = open('c.txt', 'r')

def find(a, b,r):
    global m
    if b == 10:
        if r>m:
            m = r
        return
    for i in range(11):
        if b+1<11 and arr[b+1][i]==0:continue
        if i not in l:
            l.append(i)
            find(i,b+1, r+arr[b+1][i])
            l.pop()

tc = int(input())
for sample in range(tc):
    arr = [list(map(int,input().split())) for _ in range(11)]
    m = 0

    for i in range(11):
        if arr[0][i] == 0: continue
        l = []
        l.append(i)
        find(i, 0, arr[0][i])
    print(m)