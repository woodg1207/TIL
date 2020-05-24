def solution(p):
    flag = 1
    while flag:
        visit = [False]*10
        num = str(p+1)
        for i in range(len(num)):
            if visit[int(num[i])]: 
                break
            visit[int(num[i])]=True
        else:
            if len(num)-1==i:
                flag=0
                break
        p+=1
    return p+1


Y = 1987
print(solution(Y))