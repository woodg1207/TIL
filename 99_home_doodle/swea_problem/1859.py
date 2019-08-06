import sys
sys.stdin = open('1859.txt', 'r')

t = int(input())

for sample in range(t):
    case = int(input())
    numbers = list(map(int, input().split()))
    box = []
    money = 0
    n_max = 0
    while numbers != sorted(numbers, reverse=True):
        for idx, i in enumerate(numbers):
            if i > n_max:
                n_max = i
                day = idx
                # print('max {} idx {}'.format(n_max, day))
        for i in numbers[:day]:
            money += n_max - i
            # print('money {}'.format(money))
        for i in numbers[:day+1]:
            # print(i)
            numbers.remove(i)
            n_max = 0
    print('#{} {}'.format(sample+1, money))

