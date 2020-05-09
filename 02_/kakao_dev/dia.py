def solution(gems):
    answer = []
    cnt_gem = []
    visit = {}
    for i in gems:
        if i in cnt_gem:continue
        cnt_gem.append(i)
        visit[i]=False
    g, cg = len(gems), len(cnt_gem)
    m = 100000
    for idx in range(g-cg+1): #시작점.
        flag = 0
        # visit = [False]*cg
        cnt = 0
        for i in range(idx, g):
            for j in range(cg):
                if gems[i]==cnt_gem[j]:
                    visit[j]=True
                    break
            cnt += 1
            if cnt>=m:
                flag=0
                break
            if cnt>=cg:
                C = 0
                for item in visit.values():
                    if item:
                        C+=1
                if C==cg:
                    flag = 1
                    break
        if flag:
            if cnt<m:
                m=cnt
                answer = [idx+1, idx+cnt]
    return answer

sample = ["AA", "AB", "AC", "AA", "AC"]
print(solution(sample))