import sys; sys.stdin = open('g.txt', 'r')

from collections import deque



def comb(a):
    global l, result
    flag = 0
    for i in range(a+1, N+1):
        l.append(i)
        visit[i] =True
        comb(i)
        l.pop()
        visit[i] = False
    if len(l)==N:
        return
    notl = []
    for i in range(1, N+1):
        if not visit[i]:
            notl.append(i)
    print(l, notl)
    for i in range(len(l)):
        cnt = 0
        # print(l[i])
        for j in range(len(G[l[i]])):
            if G[l[i]][j] not in l:
                cnt += 1
        if cnt == len(G[l[i]]):
            flag = 1
            break
    for i in range(len(notl)):
        cnt = 0
        # print(notl[i])
        for j in range(len(G[notl[i]])):
            if G[notl[i]][j] not in notl:
                cnt += 1
        if cnt == len(G[notl[i]]):
            flag = 1
            break
    if not flag:
        sum_a, sum_b = 0, 0 
        for i in l:
            sum_a += people[i-1]
        for i in notl:
            sum_b += people[i-1]
        re = abs(sum_a-sum_b)

        if result>re:
            result = re
    return

result = 0xffff
N = int(input())
people = list(map(int, input().split()))
G = [[False]]
for i in range(1, N+1):
    a = list(map(int, input().split()))
    G.append(a[1:])
visit = [False] *(N+1)
# print(G)
l = [1]
visit[1] = True
comb(1)
# print('result')
if result!=0xffff:
    print(result)
else:
    print(-1)