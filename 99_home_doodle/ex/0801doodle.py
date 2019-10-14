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

# class Student:
#     def __init__(self, name='홍길동', age='30'):
#         self.name = name
#         self.age = age   
    
#     def __repr__(self):
#         return f'이름은 {self.name}, 나이는 {self.age}'

# class ClassMate(Student):
#     cnt = 0
#     def __init__(self, name1, name2):
#         self.name1 = name1.name
#         self.name2 = name2.name
#         self.sum1 = int(name1.age) +int(name2.age) 
#         ClassMate.cnt += 1
    
#     def __repr__(self):
#         return f'{self.name1}과 {self.name2}는 커플이다.'

#     def display(self):
#         print(f'{self.name1}과 {self.name2}')
    
#     def sum_age(self):
#         print(self.sum1)
    
#     def how_many(self):
#         print(ClassMate.cnt)

# p1 = Student(age=10)
# p2 = Student('김ssafy',10)   
# print(p1)
# couple = ClassMate(p1, p2)
# couple.display()
# couple.sum_age()
# couple.how_many()

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.center = (self.x, self.y)

#     def __str__(self):
#         return 'Point:{}'.format(self.center)


# class Circle(Point):
#     pi = 3.14
#     def __init__(self, center, r):
#         self.center = center.center
#         self.r = r
        
#     def get_area(self):
#         self.area = 3.14*self.r**2
#         return self.area

#     def get_perimeter(self):
#         return self.r*3.14*2
    
#     def get_center(self):
#         return self.center
    
#     def __str__(self):
#         return 'Circle:{}, r:{}'.format(self.center, self.r)


# p1 = Point(0, 0) 
# c1 = Circle(p1, 3) 
# print(c1.get_area()) 
# print(c1.get_perimeter()) 
# print(c1.get_center()) 
# print(c1) 
# p2 = Point(4, 5) 
# c2 = Circle(p2, 1) 
# print(c2.get_area()) 
# print(c2.get_perimeter()) 
# print(c2.get_center()) 
# print(c2)

# def pick_and_sum(samples):
#     numbers = ''
#     result = 0
#     for sample in samples:
#         if sample.isdecimal():
#             numbers += sample
#         elif numbers:
#             result += int(numbers)
#             numbers = ''
#     return result

# print(pick_and_sum('The30quick20brown10f0x1203jumps914ov3r1349the102l4zy dog'))