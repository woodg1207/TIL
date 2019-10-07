## 피보나치를 재귀로만 계산했을 때 
def find(n):
    global cnt
    cnt += 1
    if n<2:
        return n
    else:
        return find(n-1)+find(n-2)
# 중복으로 함수를 호출 하면서 시간이 오래 걸린다. 
# 이를 해결하기위해 memoization이라는 기법을 사용한다. 
### memoization을 활용했을 때
def fibo(n):
    global cnt 
    cnt += 1
    if n>=2 and f[n]==-1:
        f[n]=fibo(n-1)+fibo(n-2)
    return f[n]

def fibo2(n):
    memo[0] = 0
    memo [1] = 1
    for i in range(2, n+1):
        memo[i] = memo[i-1]+memo[i-2]
    return memo[n]

cnt = 0
N = int(input())
f = [-1]*(N+1)
memo = [-1]*(N+1)
f[0]=0
f[1] = 1
# print(find(N))
print(fibo2(N))
print('count : ', cnt)