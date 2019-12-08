import sys
sys.stdin = open('queen.txt', 'r')

def find(a, b):
    global cnt
    if a==N-1:
        cnt += 1
        return
    for i in range(N):
        if i in l: continue
        if (i+a+1) in d:continue
        if (a+1-i) in d2: continue
        l.append(i)
        d.append(i+a+1)
        d2.append(a+1-i)
        find(a+1, i)
        l.pop()
        d.pop()
        d2.pop()

tc = int(input())
for sample in range(tc):
    N = int(input())
    cnt = 0
    for i in range(N):
        l=[]
        d = []
        d2 = []
        l.append(i)
        d.append(i+0)
        d2.append(0-i)
        find(0, i)
    print('#{} {}'.format(sample+1, cnt))