from pprint import pprint
my = [list(map(int,input().split())) for i in range(5)]
a = []
for i in range(5):
    a.extend(map(int, input().split()))

bingo = 0
while bingo < 3:
    for idx, num in enumerate(a):
        for i in range(len(my)):
            for j in range(len(my[i])):
                if my[i][j] == num:
                    my[i][j] = 0
                    cnt = idx
                if sum(my)
            if sum(my[i]) == 0:
                bingo += 1
                