import sys; sys.stdin = open('paper.txt', 'r')
from pprint import pprint

n = int(input())
papers = [list(map(int,input().split())) for _ in range(n)]
max1 = papers[0][0]+papers[0][2]
max2 = papers[0][1]+papers[0][3]
for a in range(1,n):
    if max1 < papers[a][0]+papers[a][2]:
        max1 = papers[a][0]+papers[a][2]
for b in range(1,n):
    if max2 < papers[b][1]+papers[b][3]:
        max2 = papers[b][1]+papers[b][3]
arr = [[0]*max2 for _ in range(max1)]
for p, paper in enumerate(papers):
    for i in range(len(arr)):
        if i == paper[0]:
            for j in range(len(arr[i])):
                if j == paper[1]:
                    for i_idx in range(paper[2]):
                        for j_idx in range(paper[3]):
                            arr[i+i_idx][j+j_idx] = p+1
for sample in range(n):
    cnt = 0
    for i in range(len(arr)):
        cnt += arr[i].count(sample+1)
    print('{}'.format(cnt))