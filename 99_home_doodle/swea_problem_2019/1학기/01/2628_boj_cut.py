import sys; sys.stdin = open('cut.txt', 'r')

paper = list(map(int,input().split()))
cut = int(input())
info = [list(map(int, input().split())) for _ in range(cut)]
row = [0]
column = [0]
for i in range(len(info)):
    if info[i][0]:
        row.append(info[i][1])
    else:
        column.append(info[i][1])
row.append(paper[0]); column.append(paper[1])
row.sort(); column.sort()
max_r, max_c = 0, 0
for r in range(len(row)-1):
    if max_r < row[r+1] - row[r]:
        max_r=row[r+1] - row[r]
for c in range(len(column)-1):
    if max_c < column[c+1] - column[c]:
        max_c = column[c+1] - column[c]
print(max_c*max_r)