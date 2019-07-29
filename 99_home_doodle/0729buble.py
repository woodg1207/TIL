# arr = [55, 7, 78, 12, 42]
# n = len(arr)
# for j in range(n-1, 0, -1):
#     for i in range(j):
#         if arr[i]> arr[i+1]:
#             arr[i], arr[i+1] = arr[i+1], arr[i]
# print(arr)
# for j in range(len(arr) - 1):
#     min_n = j
#     for i in range(1+min_n, len(arr)):
#         if arr[i] < arr[min_n]:
#             min_n = i
#     arr[j], arr[min_n] = arr[min_n], arr[j]
# print(arr)

# data = [0, 4, 1, 3, 1, 2, 4, 1]
# counts = [0] * 5  ##maximum = 4
# for val in data:
#     counts[val] += 1
# ##누적빈도수
# # for i in range(1, len(counts)):
# #     counts[i] += counts[i-1]
# # print(counts)
# sorte = []
# for i in range(len(counts)):
#     for j in range(counts[i]):
#         sorte.append(i)
# print(sorte)

data = 'ABC'
n = len(data)
for i in range(n):
    for j in range(n):
        if i == j: continue
        for k in range(n):
            if i == k or j==k: continue
            print(data[i], data[j], data[k])