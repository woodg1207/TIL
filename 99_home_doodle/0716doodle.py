'''
02_workshop 파이썬 파일
'''
#1
n = 5
m = 9
a='*'
for i in range(m):
    print(f'{a*n}')

#2
student = {
    'python' : 80,
    'algoritm' : 99,
    'django' : 89,
    'flask' : 83
}
sum1 = 0
cnt = 0
for point in student.values():
    cnt += 1
    sum1 += point
print(sum1/cnt)
a = sum(student.values())/len(student)
print(a)
#3
blood_types = ['A', 'B', 'A', 'O', 'AB', 'AB', 'O', 'A', 'B', 'O', 'B', 'AB']
result ={}
for i in blood_types:
    result[i] = blood_types.count(i)
print(result)
calendar = { 
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31,6: 30, 
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31 
} 
weeks = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su'] 
# 아래에 코드를 작성하세요.
for month in range(1,4):
    print(str(month)+'월')
    for i in range(len(weeks)):
        print(weeks[i], end = ' ')
    print()
    cnt = 0
    for j in range(1, len(calendar.get(month))):
        cnt+=1
        print(j, end = ' ')
            if cnt > 7:
                print()
                cnt = 0