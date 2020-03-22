import random


random_str = ''
il = ['I', 'l']
for i in range(20):
    random_str += random.choice(il)
print(random_str)