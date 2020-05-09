
def solution(v):
    
    check = []
    visit = []
    for point in v:
        flag = 0
        for i in range(len(point)):
            if [point[i], i] in check: 
                visit.append(point)
                flag = 1
                break
        if flag: continue
        for i in range(2):
            check.append([point[i], i])
    v = [False] * 4
    print(visit)
    for idx, i in enumerate(visit[0]):
        for j in range(len(check)):
            if i == check[j][0] and check[j][1]==idx:
                v[j]=True
    result = [0,0]
    for i in range(4):
        if v[i]: continue
        if check[i][1]:
            result[1]=check[i][0]
        else:
            result[0]=check[i][0]
            

    return result


sample =[[1, 1], [1, 2], [2, 1]]
print(solution(sample))