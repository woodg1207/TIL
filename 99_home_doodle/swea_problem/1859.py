import sys
sys.stdin = open('input (1).txt', 'r')

t = int(input())

for sample in range(t):
    case = int(input())
    numbers = list(map(int,input().split()))
    
    print('#{} {}'.format(sample+1, ))
    max_money = 0

    
