# 딕셔너리 반복문 활용하기
lunch = {
    '중국집': '02 0000 0000', 
    '분식집': '02 2332 2323', 
    '일식집': '02 9700 6238'
}
# 기본 활용 
# for key in lunch:
#     print(key)
#     print(lunch[key])#value값 나오게 하는 방법 print(lunch.get(key))
   
for key, value in lunch.items(): ## 한번에 나오게 하는 방법 
    print(key, value)

#value만 갖고오기
for value in lunch.values():
    print(value)
#key만 갖고오기
for key in lunch.keys():
    print(key)