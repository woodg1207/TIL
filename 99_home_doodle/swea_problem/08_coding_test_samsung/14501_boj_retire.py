import sys; sys.stdin = open('r.txt', 'r')

def find(a):
    global m, M
    if a + day[a] > N+1: return
    if M < m:
        M = m
    for idx in range(a+day[a], N+1):
        m += money[idx]
        find(idx)
        m -= money[idx]

N = int(input())
day = [0]* (N+1)
money = [0] * (N+1)
for _ in range(1, N+1):
    a, b = map(int, input().split())
    day[_] = a
    money[_] = b
M = 0
for i in range(1, N+1):
    if i + day[i] > N+1: continue
    m = money[i]
    find(i)
print(M) 
