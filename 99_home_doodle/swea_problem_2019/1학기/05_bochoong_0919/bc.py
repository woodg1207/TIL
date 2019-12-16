#재귀함수 호출 트리

#부분 집합을 생성
# 원소의 수 == N
# N 번의 선택을 통해서 부분집합 생성, 각각의 원소에 대해서
# 매번 선택할 때의 선택지 ==> 2개
path = [0]*3
def subset(k, n):
    if k== n:
        # print(path)
        return
    #함수 호출이 선택이다.
    path[k] = 1; subset(k+1, n)
    path[k] = 0; subset(k+1, n)

subset(0,3)
#이진 트리의 특성 3계층이라면 2**4-1=(1 + 2**1 + 2**2 + 2**3)개의 노드가 존재한다.

#순열 생성
# 모든 순열을 생성하는 과정을 선택의과정
N = 3
visit = [0]*3
for i in range(N):
    visit[i] = 1
    #-----------
    for j in range(N):
        if visit[j]:
            continue
        visit[j] = 1 # 방문처리
        for k in range(N):
            if visit[k]: continue
            visit[k] = 1
            # print(i, j, k)
            visit[k] =0  # 원상복귀
        visit[j] = 0
    visit[i] = 0
N = 3
visit = [0]*3
#재귀호출로 순열생성
order = []
def perm(k,n):
    if k == n:
        # print(order)
        return
    for i in range(N):
        if visit[i] == 1:continue
        visit[i] = 1
        order.append(i)
        perm(k+1, n)
        order.pop()
        visit[i] = 0
perm(0, N)

# 조합 생성
arr = 'ABCDE'
N=5
for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            # print(arr[i],arr[j],arr[k])
            pass
# 조합 재귀함수

arr = 'ABCDE'
N, R=5, 3
choose = []
def comb(k, s): #  s : 선택할 요소의 시작값
    if k==R:
        print(choose)
        return
    for i in range(s, N):
        choose.append(arr[i])
        comb(k+1, i+1)
        choose.pop()
comb(0, 0)

# 중복조합이라면
N = 3
for i in range(N):
    for j in range(i, N):
        print(i, j)