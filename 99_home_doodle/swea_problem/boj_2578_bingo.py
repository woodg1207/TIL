from pprint import pprint
import sys; sys.stdin = open('bingo.txt', 'r')

arr = [list(map(int,input().split())) for i in range(5)]
t = []
for i in range(5):
    t.extend(map(int, input().split()))
row = []
column = []
diag1 = []
diag2 = []
while t:
    bingo = 0
    n = t.pop(0)
    for i in range(5):
        for j in range(5):
            if arr[i][j] == n:
                arr[i][j] = 0
            row.append(arr[i][j])
            column.append(arr[j][i])
            if row.count(0) == 5:
                bingo += 1
                if bingo == 3:
                    reusult = 25-len(t)
            if column.count(0) == 5:
                bingo += 1
                if bingo == 3:
                    reusult = 25-len(t)
        else:
            row.clear()
            column.clear()
        diag1.append(arr[i][i])
        diag2.append(arr[i][4-i])
        if diag1.count(0) == 5:
            bingo += 1
            if bingo == 3:
                    reusult = 25-len(t)
        if diag2.count(0) == 5:
            bingo += 1
            if bingo == 3:
                    reusult = 25-len(t)       
    else:
        diag1.clear()
        diag2.clear()
    if bingo >= 3:

        break

print(reusult)
