import sys; sys.stdin = open('t.txt', 'r')

tc = int(input())
for sample in range(tc):
    N, X, Y = map(int, input().split())
    strN = str(N)
    n = len(strN)
    result = 0
    flag = 0
    for i in range(n):
        num = int(strN[i])
        if num <= X:
            pre = X - num
            if pre:
                pass
            else:
                result = result*10 + X

        elif X < num < Y:
            result = result * 10 + X
            pre = int(strN[i])-X
            if pre:
                for j in range(n-i-1):
                    result = result*10 + Y
                break
        elif Y <= num:
            result = result*10 +Y
            pre = int(strN[i]) -Y
            if pre:
                for j in range(n-i-1):
                    result = result*10 +Y
                break

    if result == 0:
        result = -1
    print('#{} {}'.format(sample+1, result))

