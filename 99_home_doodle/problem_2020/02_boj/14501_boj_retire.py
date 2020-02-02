import sys; sys.stdin = open('r.txt', 'r')

N = int(input())
info = [list(map(int, input().split())) for _ in range(N)]
M = 0

def work(day):
    global money, M
    if day >N:return
    if money > M:
        M = money
    for i in range(day, N):
        if  info[i][0] > N: continue
        money += info[i][1]
        work(i+ info[i][0])
        money -= info[i][1]

for i in range(N):
    if i + info[i][0] > N: continue
    money = info[i][1]
    work(i + info[i][0])
print(M)