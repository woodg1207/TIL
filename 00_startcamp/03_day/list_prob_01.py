str_ex = input('input string : ')
i = 0
for last_str in str_ex:
    i = i+1
print(f'{str_ex[0]} and {str_ex[i-1]}')

###
# num_n = int(input('자연수 입력'))
# for num in range(num_n):
#     print(f'{num+1}')

###
# num_n = int(input('자연수 입력'))
# if num_n % 2 ==1:  
# ## if num_n %2 한 결과값이 1이 나오면 트루값이기때문에 트루면 지나가는 개념으로도 가능
#     print('홀수')
# else:
#     print('짝수')

##
# kor = int(input('국어 : '))
# eng = int(input('영어 : '))
# math = int(input('수학 : '))
# sci = int(input('과학 : '))

# if kor >=90 and eng >80 and math > 85 and sci >=80:
#     print(True)
# else:
#     print(False)

###
prices = input('물품 가격을 입력하세요: ')
price_lists = prices.split(';') #;를 기준으로 리스트 구분
## list.append(1) >> 리스트에 1을 추가한다. 
boxes = []  ##빈 리스트를 만들어주는 것도 습관
for price_list in price_lists:
    boxes.append(int(price_list)) #빈 박스에 리스트를 넣어준다.

print(boxes)
boxes.sort(reverse=True) #정렬하는 과정 
for box in boxes:
    print(box)