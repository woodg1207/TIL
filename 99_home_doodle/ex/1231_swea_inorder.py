import sys; sys.stdin = open('i.txt','r')

def inorder(a):
    # print(a)
    if a!=0:
        inorder(c[a][1])
        print(c[a][0], end= '')
        inorder(c[a][2])


for sample in range(10):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    c = [[0]*3 for _ in range(N+1)]
    # print(c[int(arr[1][0])][1])
    for i in range(N):
        if len(arr[i]) == 4:
            c[int(arr[i][0])][0]=arr[i][1]
            c[int(arr[i][0])][1]=int(arr[i][2])
            c[int(arr[i][0])][2]=int(arr[i][3])
        elif len(arr[i]) == 3:
            c[int(arr[i][0])][0]=arr[i][1]
            c[int(arr[i][0])][1]=int(arr[i][2])
        else:
            c[int(arr[i][0])][0]=arr[i][1]
    # print(c)
    print('#{}'.format(sample+1), end= ' ')
    inorder(1)
    print()