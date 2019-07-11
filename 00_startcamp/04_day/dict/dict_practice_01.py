"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
sum_1 = 0
for subject_score in scores.values():
    sum_1 = sum_1 + subject_score  # sum += subject_score
mean = float(sum_1/len(scores))##딕셔너리의 길이를 알수있는 함수 len(dict)
print(mean)




# 2. 반 평균을 구하시오. -> 전체 평균
scores = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}

# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')
sum_a = 0
sum_b = 0
for subject_score in scores.get('a').values():
    sum_a += subject_score
for subject_score in scores.get('b').values():
    sum_b += subject_score
mean = (sum_a + sum_b)/(len(scores.get('b'))+len(scores.get('a')))
print(mean)
'''
i = 0
for person_score in scores.values():
    for indivi in personscore.values():
        total_score += indivi
        i+=1
mean = total_score / i
'''
# 3. 도시별 최근 3일의 온도입니다.
city = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""
sum_seoul = 0
seoul = city['서울']##city.get('서울')랑 비슷한표현
d = city['대전']
g = city['광주']
b = city['부산']
for i in seoul:
    sum_seoul += i
mean = sum_seoul / len(seoul)
print(f'{round(mean, 2)}')
sum_seoul = 0
for i in d:
    sum_seoul += i
mean = sum_seoul / len(d)
print(f'{round(mean, 2)}')
sum_seoul = 0
for i in g:
    sum_seoul += i
mean = sum_seoul / len(g)
print(f'{round(mean, 2)}')
sum_seoul = 0
for i in b:
    sum_seoul += i
mean = sum_seoul / len(b)
print(f'{round(mean, 2)}')

for name, temp in city.items():
    avg_temp = sum(temp)/ len(temp)
    print(f'{name}:{avg_temp:.2f}')





# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
for name, temp in city.items():
    #첫번째 시행때 
    #name = '서울'
    #temp = [-6, -10, 5]
    #단한번만 실행되는 조건이 필요 
        if count == 0:
            hot_temp = max(temp)
            cold_temp = min(temp)
            hot_city = name
            cold_city = name
        else:
            pass
            #최저온도가 cold_temp보다 낮으면, cold_temp에 넣고
        if min(temp) < cold_temp:
            cold_temp = min(temp)
            cold_city = name
        #최고온도가 hot_temp 보다 높으면, hot_temp에 넣는다. 
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
        count +=1 
print(f'추운곳은{cold_city}, 더운곳은{hot_city}')


# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')


if 2 in city['서울']:
    print(f'있어요')
else:
    print('없어요')