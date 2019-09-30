import sys
sys.stdin = open('seven.txt', 'r')


def comb(a, b):
    global m, cnt
    if b == 7:
        for i in range(7):
            flag = 1
            for j in range(7):
                if m[i] + 1 == m[j] and (m[i]+1)%5!=0:
                    flag = 0
                elif m[i] + 5 == m[j]:
                    flag = 0
                elif m[i] - 1 == m[j] and m[i]%5!=0:
                    flag = 0
                elif m[i] - 5 == m[j]:
                    flag = 0
            if flag:
                return
        c = 0
        for i in range(7):
            if m[i] in s:
                c+=1
        if c<b-3:
            return
        cnt +=1
        return
    if b>=2:
        for i in range(len(m)):
            flag = 1
            for j in range(len(m)):
                if m[i] + 1 == m[j] and (m[i]+1)%5!=0:
                    flag = 0
                elif m[i] + 5 == m[j]:
                    flag = 0
                elif m[i] - 1 == m[j] and m[i]%5!=0:
                    flag = 0
                elif m[i] - 5 == m[j]:
                    flag = 0
            if flag:
                return
    if b >= 4:
        c = 0
        for i in range(len(m)):
            if m[i] in s:
                c+=1
        if c<b-3:
            return
    for i in range(a+1, 25):
        if visit[i]: continue
        visit[i] = True
        m.append(i)
        comb(i, b+1)
        m.pop()
        visit[i] = False

arr=[[i for i in input()] for _ in range(5)]
number = [[i for i in range(5*(j), 5*(j+1))] for j in range(5)]
visit = [False] * (25)
cnt = 0
s = []
for i in range(5):
    for j in range(5):
        if arr[i][j] == 'S':
            s.append(number[i][j])
for i in range(19):
    if i != 5: continue
    m = []
    visit = [False] * (25)
    visit[i] = True
    m.append(i)
    comb(i, 1)
print(cnt)