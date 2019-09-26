import sys
sys.stdin = open('e.txt', 'r')

def find(a, b):
    global m, re
    if b == 6:
        re = 0
        for i in range(6):
            re += abs(robot[i][0]-c[l[i]][0])+abs(robot[i][1]-c[l[i]][1])
        if m > re:
            m = re
        return
    for i in range(6):
        if i in l: continue
        l.append(i)
        find(a, b+1)
        l.pop()

tc = int(input())
for sample in range(tc):
    number = int(input())
    arr=[list(map(int, input().split())) for _ in range(10)]
    robot = []
    c = []
    m = 20
    for i in range(10):
        for j in range(10):
            if arr[i][j] == 9:
                robot.append([i, j])
            elif arr[i][j] != 0:
                c.append([i, j])
    for i in range(6):
        re = 0
        l = []
        l.append(i)
        find(i, 1)
    print('#{} {}'.format(number, m))