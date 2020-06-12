from copy import deepcopy
calcul = []
def comb(n, cnt, cal_list):
    if cnt == n:
        data = deepcopy(cal_list)
        calcul.append(data)
        return calcul
    cal_list.append(0)
    comb(n, cnt+1,cal_list)
    cal_list.pop()
    cal_list.append(1)
    comb(n, cnt+1,cal_list)
    cal_list.pop()
    return calcul
    

def solution(numbers, target):
    l = comb(len(numbers), 0, [])
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
print(solution(N, T))