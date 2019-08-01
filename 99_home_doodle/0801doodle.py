# def my_join(sample_list, arg):
#     new_str = ''
#     for sample in sample_list[:-1]:
#         new_str += sample + arg
#     new_str += sample_list[-1]
#     return new_str
# print(my_join('배고파', '.'))
# print(my_join(['1', '2', '3'], ''))

# def solve(words):
#     cnt = 0
#     for word in words:
#         if word.isupper():
#             cnt += 1
#     if cnt > (len(words)/2):
#         words = words.upper()
#     else:
#         words = words.lower()
#     return words

# print(solve('coDe'))
# print(solve('CODe'))
# print(solve('coDE'))

# def unused_digits(*args):
#     numbers = '0123456789'
#     result = ''
#     string = ''.join(list(map(str,args)))
#     for num in numbers:
#         if num not in string:
#             result += num
#     return result

# print(unused_digits(12, 34, 56, 78))
# print(unused_digits(2015, 8, 26))
# def even_and_odd(samples):
#     samples = sorted(list(set(samples)))
#     new_samples = []
#     even = []
#     odd = []
#     for sample in samples:
#         if sample % 2:
#             odd.append(sample)
#         else:
#             even.append(sample)
#     even = even[::-1]
#     if len(odd) > len(even):
#         for i in range(len(even)):
#             new_samples.append(even.pop())
#             new_samples.append(odd.pop())
#         odd = odd[::-1]
#         new_samples.extend(odd)
#     else:
#         for i in range(len(odd)):
#             new_samples.append(even.pop())
#             new_samples.append(odd.pop())
#         even = even[::-1]
#         new_samples.extend(even)
#     return new_samples

# print(even_and_odd([7, 3, 14, 17]))
# print(even_and_odd([1, 3, 5, 7, 9, 11]))
# print(even_and_odd([1, 2, 2, 4, 4, 6, 6, 2004, 9, 11]))

class Student:
    def __init__(self, name='홍길동', age='30'):
        self.name = name
        self.age = age   
    
    def __repr__(self):
        return f'이름은 {self.name}, 나이는 {self.age}'

class ClassMate(Student):
    cnt = 0
    def __init__(self, name1, name2):
        self.name1 = name1.name
        self.name2 = name2.name
        self.sum1 = int(name1.age) +int(name2.age) 
        ClassMate.cnt += 1
    
    def __repr__(self):
        return f'{self.name1}과 {self.name2}는 커플이다.'

    def display(self):
        print(f'{self.name1}과 {self.name2}')
    
    def sum_age(self):
        print(self.sum1)
    
    def how_many(self):
        print(ClassMate.cnt)

p1 = Student(age=10)
p2 = Student('김ssafy',10)   
print(p1)
couple = ClassMate(p1, p2)
couple.display()
couple.sum_age()
couple.how_many()
