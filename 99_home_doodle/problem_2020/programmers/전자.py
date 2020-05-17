b = 0
i = 1
cnt = 0
while b<=10:
    cnt += 1
    b += i
    i += 1
    print('{}번째 while : b={}, i={}'.format(cnt, b,i))
print('i={}, b={}'.format(i,b))