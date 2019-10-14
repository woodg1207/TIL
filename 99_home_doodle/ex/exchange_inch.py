##1.인치를 cm로 변환

# inch = float(input('인치를 입력하시오'))
# cm = inch * 2.54
# print(f'{inch:.2f} inch  => {cm} cm')

##2.kg을 파운드로 변환하는 프로그램 
#소수점 반올림은 round(변수, 자리수)

# kilo = float(input('킬로그램을 입력하세요'))
# lb = kilo * 2.2046
# print(f'{round(kilo,2)}kg => {round(lb,2)}lb')

##3.섭씨를 화씨로 변경
# do_c = float(input('입력해라'))
# do_f = (do_c * 1.8) + 32
# print(f'{do_c} => {round(do_f, 3)}')
##4.화씨를 섭씨로 변경
# do_f = float(input('insert'))
# do_c = (do_f - 32) / 1.8
# print(f'{do_f} => {round(do_c,2)}')
###
# salt_water = 100
# water = 200
# salt = float(salt_water*0.2)
# print(salt)
# combine = float(salt/(salt_water+water)*100)
# print(f'혼합된 소금물의 농도: {round(combine, 2)}%')

###약수구하기 문제 ++추가 소수면 말해주기 
# num = int(input(''))
# boxes = []  빈리스트를 만들어주는것이 중요하다. 
# for i in range(num):
#     if num % (i+1) == 0:
#         boxes.append(i+1)
#         print(f'{i+1}(은)는 {num}의 약수입니다.')
# if len(boxes) == 2:
#     print(f'{num}(은)는 {boxes[0]}과 {boxes[1]}로만 나눌 수 있는 소수입니다.')
###소문자 대문자 판별 문제
# alpha = input('')
# if alpha.upper() == alpha:
#     print(f'{alpha} 는 대문자 입니다.')
# else:
#     print(f'{alpha} 는 소문자 입니다.')

##
import random
game = ['가위', '바위', '보']
man1 = random.choice(game)
print(man1)
man2 = random.choice(game)
print(man2)
if man1 == man2:
    print(f'Result : Draw')
elif game.index(man1)-1 == game.index(man2) or game.index(man1)+2 == game.index(man2):
    print(f'Result : Man1 Win!')
else:
    print(f'Result : Man2 Win!')

