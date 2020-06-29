
def solution(numbers, target):
    n = len(numbers)
    cnt = 0
    for i in range(2**n):
        number = 0
        num = bin(i)[2:]
        extra = n-len(num)
        result = '0'*extra + num
        for j in range(len(result)):
            if result[j]=='1':
                number += numbers[j]
            else:
                number -= numbers[j]
        if number == target:
            cnt += 1


    return cnt



N = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]
T = 3
print(solution(N, T))
