import sys
sys.stdin = open('seven.txt', 'r')

def find(a, b, c, d):
    global m
    if d >= 4:
        if d-c.count('S')>3:
            return
    if d == 7:
        # print(c)
        l = []
        if c.count('S')<4: return
        # print(c)
        for i in range(len(visit)):
            if visit[i]:
                l.append(i)
        # print(l)
        if l not in m:
            m.append(l)
        return
    
    if a+1<5:
        if visit[number[a+1][b]]==False:
            visit[number[a+1][b]] = True
            find(a+1, b, c+arr[a+1][b],d+1)
            visit[number[a+1][b]] = False
        else:
            find(a+1,b,c+arr[a+1][b],d)
    if a-1>=0:
        if visit[number[a-1][b]] == False:
            visit[number[a-1][b]] = True
            find(a-1, b, c+arr[a-1][b], d+1)
            visit[number[a-1][b]] = False
        else:
            find(a-1, b, c+arr[a-1][b], d)
    if b+1<5:
        if not visit[number[a][b+1]]:
            visit[number[a][b+1]] = True    
            find(a, b+1, c+arr[a][b+1], d+1)
            visit[number[a][b+1]] = False
        else:
            find(a, b+1, c+arr[a][b+1], d)
    if b-1>=0:
        if not visit[number[a][b-1]]:
            visit[number[a][b-1]] = True
            find(a, b-1, c+arr[a][b-1], d+1)
            visit[number[a][b-1]] = False
        else:
            find(a, b-1, c+arr[a][b-1], d)
        
    
arr=[[i for i in input()] for _ in range(5)]
number = [[i for i in range(5*(j), 5*(j+1))] for j in range(5)]
m = []
for i in range(5):
    for j in range(5):
        visit = [False] * (25)
        visit[number[i][j]] = True
        find(i, j, arr[i][j], 1)
print(len(m))




# def find(a, b, c, d, e):
#     global m
#     if d == 7:
#         # print(c)
#         l = []
#         if c.count('S')<4: return
#         # print(c)
#         for i in range(len(visit)):
#             if visit[i]:
#                 l.append(i)
#         print(l)
#         if l not in m:
#             m.append(l)
#         return
#     # for i in range(25):
#     #     find()
    
# def comb(a, b):
#     if b == 7:
#         for i in range(7):
#             flag = 1
#             for j in range(7):
#                 if i == j: continue
#                 if l[j]-1<=l[i]<=l[j]+1:
#                     flag = 0
#                 if l[i]

#         return
#     for i in range(a+1,25):
#         l.append(i)
#         comb(i, b+1)
#         l.pop()
        
    
# arr=[[i for i in input()] for _ in range(5)]
# number = [[i for i in range(5*(j), 5*(j+1))] for j in range(5)]
# m = []
# for i in range(25-7):
#     l = []
#     l.append(i)
#     comb(i, 1)



# for i in range(5):
#     for j in range(5):
#         visit = [False] * (25)
#         visit[number[i][j]] = True
#         find(i, j, arr[i][j], 1, number[i][j])
# print(len(m))