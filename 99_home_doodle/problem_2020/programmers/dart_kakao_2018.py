
point_dict = {
    'S':1,
    'D':2,
    'T':3,
}
num = '1234567890'
option = '*#'
def solution(dartResult):
    answer = 0
    point = ''
    point_list = []
    for idx, n in enumerate(dartResult):
        if n in num: # 숫자 판별
            point += n
        else:
            if point: 
                point_list.append(int(point))
                point = ''            
            if n not in option:
                point_list[-1] = point_list[-1] ** point_dict[n]
            else:
                l = len(point_list)
                if n == '*':
                    if l == 1:
                        point_list[l-1] = point_list[l-1] * 2
                    else:
                        point_list[l-2] = point_list[l-2] * 2
                        point_list[l-1] = point_list[l-1] * 2
                else:
                    point_list[l-1] = point_list[l-1] * -1
    return sum(point_list)


testcase = '1D2S#10S'
print(solution(testcase))