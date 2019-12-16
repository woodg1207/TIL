import sys
sys.stdin = open('sum.txt', 'r')

def find(a, re):
    global k, cnt
    if re == k:
        cnt += 1
        return
    if re > k:
        return
    for i in range(a+1, n):
        find(i, re+arr[i])

tc = int(input())
for sample in range(tc):
    n, k = map(int,input().split())
    arr = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        find(i, arr[i])
    print('#{} {}'.format(sample+1, cnt))