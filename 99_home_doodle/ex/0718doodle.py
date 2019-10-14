import math
math.sqrt(2)

def my_sqrt(n):
    x, y = 1, n
    result = 1
    while abs(result**2 - n) > 1e-10: 
    # while not math.isclose(result**2, n): 
    # 제곱근의 제곱 result**2 과 입력값 n 의 차이가 적어도 이 정도차이보다 작아지면!
        result = (x+y) / 2 #양쪽 끝 값을 더해서 2로 나눈다.
        # 위 근사치에 따라 x 또는 y의 값을 바꾼다.
        if result**2 < n:
            x = result
        else:
            y = result
    return result


print(my_sqrt(4))

def isqrt(n):

    x = n

    y = (x+1)/2

    while y < x:

        x = y

        y = (x+n/x)/2

    return x




    