import sys
sys.stdin = open('l.txt', 'r')

def find(a, b):
    if b == 6:
        print(*l)
        return
    for i in range(a+1, arr[0]+1):
        l.append(arr[i])
        find(i, b+1)
        l.pop()

while 1:
    arr = list(map(int, input().split()))
    if arr[0] == 0:
        break
    for i in range(1, arr[0]-4):
        l = []
        l.append(arr[i])
        find(i, 1)
    print()