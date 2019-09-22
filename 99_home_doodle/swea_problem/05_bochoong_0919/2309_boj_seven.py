import sys
sys.stdin = open('s.txt', 'r')

def find(a, b):
    if b == 7:
        re = sum(l)
        if re==100:
            l.sort()
            for i in l:
                print(i)
        return
    for i in range(a+1, 9):
        l.append(arr[i])
        find(i, b+1)
        l.pop()

arr = [int(input()) for _ in range(9)]
for i in range(3):
    l=[]
    l.append(arr[i])
    find(i, 1)
