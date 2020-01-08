import sys
sys.stdin = open('b.txt', 'r')


def find(a, b):
    global ma
    if b == 3:
        re = sum(l)
        if m>=re and ma<re:
            ma = re            
        return
    for i in range(a+1, n):
        l.append(cards[i])
        find(i, b+1)
        l.pop()

n, m = map(int, input().split())
cards = list(map(int, input().split()))
ma = 0
for i in range(n):
    l = []
    l.append(cards[i])
    find(i, 1)
print(ma)