import sys; sys.stdin = open('test_02.txt', 'r')

def shuffle(arr, cnt):
    global n
    if cnt == 4:
        return -1
    for i in range(n):
        a = arr[:n // 2]
        b = arr[n // 2:]
        m = []
        re = []
        a_s = []
        b_s = []
        if i <= n//2:
            for idx in range(i):
                a_s.append(a.pop())
                b_s.append(b.pop(0))
            for _ in range(i):
                m.append(b_s.pop(0))
                m.append(a_s.pop())
            re.extend(a)
            re.extend(m)
            re.extend(b)
        else:
            j = i - (n//2)
            for _ in range(j):
                a_s.append(a.pop(0))
                b_s.append(b.pop())
            for _ in range(j):
                m.append(a_s.pop(0))
                m.append(b_s.pop())
            re.extend(b)
            re.extend(m)
            re.extend(a)
        if re == list(range(1,n+1)) or re == list(range(1, n+1))[::-1]:
            return cnt+1
        elif i:
            shuffle(re, cnt + 1)

testcase = int(input())
for sample in range(testcase):
    n = int(input())
    cards = list(map(int, input().split()))
    print('#{} {}'.format(sample+1, shuffle(cards,0)))
