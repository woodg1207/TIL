name = '우동균'
ex = f'sjdkfjsklfdjkj{name}'
# print(ex)
# print(f'안녕하세요, {name}입니다.')


#점심메뉴 추천
import random

menu = ['돈까스', '라면', '빵']
lunch = random.choice(menu)
# print(f'오늘의 점심 메뉴는 {lunch}입니다.')

#lotto

numbers = range(1, 46)

lotto = random.sample(numbers, 6)
print(f'오늘의 당첨 번호는 {sorted(lotto)}입니다.')#중괄호 안에서 함수를 사용할 수 있다. 

#필요하면 이렇게 할 수 있다. 
name = '홍길동'
print('안녕하세요.'+ name+'입니다.')