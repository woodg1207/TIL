import sys
sys.stdin = open('pass.txt', 'r')

# def find(a, b):
#     # print(l)
#     if b==L:
#         for i in l:
#             print(alpha[i], end='')
#         print()
#         return
#     if l[-1]>must[-1]:
#         flag = 1
#         # print(l)
#         for i in range(len(l)):
#             if l[i] in must:
#                 flag = 0
#         if flag:
#             return
#     for i in range(a+1, C):
#         l.append(new_arr[i])
#         find(i, b+1)
#         l.pop()    
# L, C = map(int, input().split())
# arr = input().split()
# alpha = 'abcdefghijklmnopqrstuvwxyz'
# beta = [0,4,8,14,20]
# new_arr = []
# for j in range(C):
#     for i in range(len(alpha)):
#         if arr[j] == alpha[i]:
#             new_arr.append(i)
# new_arr.sort()
# must = []
# for i in new_arr:
#     if i in beta:
#         must.append(i)
# for i in range(C):
#     if new_arr[i]>must[-1]:
#         break
#     l = []
#     l.append(new_arr[i])
#     find(i, 1)

def find(a, b):
    if b==L:
        for i in l:
            print(new_arr[i], end='')
        print()
        return
    if l[-1]>must[-1]:
        flag = 1
        # print(l)
        for i in range(len(l)):
            if l[i] in must:
                flag = 0
        if flag:
            return
    for i in range(a+1, C):
        l.append(i)
        find(i, b+1)
        l.pop()    

L, C = map(int, input().split())
arr = input().split()
alpha = 'abcdefghijklmnopqrstuvwxyz'
beta = 'aeiou'
new_ = []
for j in range(C):
    for i in range(len(alpha)):
        if arr[j] == alpha[i]:
            new_.append(i)
new_.sort()
new_arr = []
must = []
for i in range(C):
    for j in range(len(alpha)):
        if new_[i]==j:
            new_arr.append(alpha[j])
for i in range(C):
    if new_arr[i] in beta:
        must.append(i)
for i in range(C):
    if i>must[-1]:
        break
    l = []
    l.append(i)
    find(i, 1)