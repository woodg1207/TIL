import sys; sys.stdin = open('c.txt', 'r')
from pprint import pprint

# from copy import deepcopy


def attack(arc, line):
    attacked = [[False]*(M) for _ in range(N)]
    # for i in arc:
    #     for mop in mops:
    # D 안에들어오는 mop은 리스트로 추가를 하고 (i, j, D) 
    # 거리가 작은 애들중에서 j값이 작은 애로 공격을 한다..
    return




def archer_position(x, depth):
    if depth==3:
        # print(archer)
        attack(archer, 0)
        return
    for i in range(x+1, M):
        archer.append([M, i])
        archer_position(i, depth+1)
        archer.pop()

N, M, D = map(int, input().split())
Map = [list(map(int, input().split())) for _ in range(N)]
Map.append([0]*M)
mops = []
for i in range(N):
    for j in range(M):
        if Map[i][j]:
            mops.append((i, j))
print(mops)
for i in range(M):
    archer = [[M,i]]
    archer_position(i, 1)