import sys
sys.stdin = open('t1926.txt', 'r')

n = int(input())
numbers = list(map(str, range(1, n+1)))
box = []
cnt = 0
for i in numbers:
    box.append(i)
for i in range(len(box)):
    for j in range(len(box[i])):
        if not int(box[i][j])%3 and int(box[i][j]):
            cnt += 1
    if cnt:
        box[i] = '-'*cnt
        cnt = 0
print(' '.join(box))