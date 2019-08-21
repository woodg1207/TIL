# arr = [i for i in range(8)]
# n = len(arr)
# m = 4

# for i in range(0, n-m+1):
#     for j in range(i, i+m):
#         print(arr[j], end=' ')
#     print()

# i = 0
# while i <= n-m:
#     print(arr[i:i+m])
#     i += 1
arr = [i for i in range(4)]
n = len(arr)

for start in range(0, n):
    for end in range(n - 1, start - 1, -1):

        for i in range(start, end + 1):
            print(arr[i], end=' ')
        print()
for start in range(0, n):
    for end in range(n - 1, start - 1, -1):

        i = start
        while i <= end:
            print(arr[i], end=' ')
            i += 1
        print()