
def solution(numbers, target):
    l=[]
    cnt = 0
    for i in range(len(l)):
        result = 0
        for j in range(len(l[i])):
            if l[i][j]:
                result += numbers[j]
            else:
                result -= numbers[j]
            if not (result<1000):
                break
        if result == target:
            cnt += 1
    return cnt



N = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
T = 3
# print(solution(N, T))
print(bin(2**4-1))