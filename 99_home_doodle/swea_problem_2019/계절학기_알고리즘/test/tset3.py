import sys; sys.stdin = open('t.txt', 'r')


def find(cnt, a, re):
    global M
    if M < re <= N:
        M = re
    if cnt == n:
        if re > N:
            return
        if M < re:
            M = re
        return
    if cnt>n-1 and int(strN[:cnt]) < re:
        return
    for i in a:
        find(cnt+1, a, re*10 + i)
    return

tc = int(input())
for sample in range(tc):
    N, X, Y = map(int, input().split())
    strN = str(N)
    n = len(strN)
    M = 0
    find(0, [X,Y], 0)
    if M == 0: M = -1
    print('#{} {}'.format(sample+1, M))