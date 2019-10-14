import sys; sys.stdin = open('r.txt', 'r')

def find(a):
    if a + day[a] >= N+1: return
    visit[a] = True
    find(a + day[a])

N = int(input())
money = []
day = []
for _ in range(N):
    a, b = map(int, input().split())
    day.append(a)
    money.append(b)
print(day, money)
for i in range(N):
    if day[i] + i > N+1: continue
    visit = [False] * (N+1)
    find(i)
    print(visit)