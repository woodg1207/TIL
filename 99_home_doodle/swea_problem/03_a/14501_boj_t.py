import sys; sys.stdin = open('t.txt', 'r')

n = int(input())
info = [list(map(int, input().split())) for _ in range(n)]
info.insert(0, 0)
stack = []
for i in range(1, n+1):
    if i+info[i][0] <= n:
        stack.append([i, info[i][0]])
while stack:
    d = stack.pop() # 첫 일정
    m = []
    m.append(info[d[0]][1])
    for i in range(d[0]+d[1],n+1): # 다음일정
        if info[i][1]
