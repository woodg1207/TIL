import sys; sys.stdin = open('sw.txt', 'r')

num = int(input())
switch = list(map(int,input().split()))
number = int(input())
students = [list(map(int,input().split())) for _ in range(number)]
# 남자는 1 여자는 2
for student in students:
    if student[0] % 2:#남
        for i in range(student[1]-1, num, student[1]):
            if (i+1) % student[1]==0:
                if switch[i]:
                    switch[i] = 0
                else:
                    switch[i] = 1
    else:
        s = student[1] - 1
        e = len(switch) - student[1]
        if s > e:
            min_idx = e
        else:
            min_idx = s
        for idx in range(1, min_idx+1):
            if switch[student[1]-1+idx] == switch[student[1]-1-idx]:
                switch[student[1]-1+idx] += 1
                switch[student[1]-1-idx] += 1
            else:
                break
        switch[student[1]-1] += 1
        for i in range(num):
            switch[i] = switch[i]%2
for i in range(num):
    print(switch[i], end=' ')
    if not (i+1)%20:
        print()