from collections import deque

def solution(total_sp, skills):
    tree = [[0] for _ in range(len(skills)+2)]
    # print(tree)
    for i in range(len(skills)):
        if tree[skills[i][0]] == [0]:
            tree[skills[i][0]] = [skills[i][1]]
        else:
            tree[skills[i][0]].append(skills[i][1])
    q = deque()
    # 최상위 찾기.
    for i in range(len(tree)):
        visit = [0]* (len(skills)+2)
        if tree[i]==[0]:
            continue
        q.append(i)
        while q:
            n = q.popleft()
            visit[n] = 1
            for j in tree[n]:
                if j ==0: continue
                q.append(j)
        if sum(visit)==len(visit)-1:
            upskill = i
            break
    cnt = [0]*(len(skills)+2)
    visit = [False]*(len(skills)+2)
    s = [upskill]
    while s:
        n = s.pop()
        if tree[n]==[0]:
            cnt[n]=1
        else:
            if visit[n]: 
                for x in tree[n]:
                    cnt[n]+=cnt[x]
                continue
            s.append(n)
            visit[n]=True
            for i in range(len(tree[n])):
                # if tree[n][i]==0:
                #     cnt[tree[n][i]] = 1
                # else:
                s.append(tree[n][i]) 
    r = sum(cnt)
    p = total_sp//r  
    l=[]
    for i in cnt[1:]:
        l.append(i*p)
    

    return l

T, S = 121,[[1, 2], [1, 3], [3, 6], [3, 4], [3, 5]]
print(solution(T, S))