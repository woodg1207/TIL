def my_join(sample_list, arg):
    new_str = ''
    for sample in sample_list[:-1]:
        new_str += sample + arg
    new_str += sample_list[-1]
    return new_str
print(my_join('배고파', '.'))
print(my_join(['1', '2', '3'], ''))

def solve(words):
    cnt = 0
    for word in words:
        if word.isupper():
            cnt += 1
    if cnt > (len(words)/2):
        words = words.upper()
    else:
        words = words.lower()
    return words

print(solve('coDe'))
print(solve('CODe'))
print(solve('coDE'))

def unused_digits(*args):
    numbers = '0123456789'
    result = ''
    string = ''.join(list(map(str,args)))
    for num in numbers:
        if num not in string:
            result += num
    return result

print(unused_digits(12, 34, 56, 78))
print(unused_digits(2015, 8, 26))
def even_and_odd(samples):
    samples = sorted(list(set(samples)))
    new_samples = []
    even = []
    odd = []
    for sample in samples:
        if sample % 2:
            odd.append(sample)
        else:
            even.append(sample)
    even = even[::-1]
    if len(odd) > len(even):
        for i in range(len(even)):
            new_samples.append(even.pop())
            new_samples.append(odd.pop())
        odd = odd[::-1]
        new_samples.extend(odd)
    else:
        for i in range(len(odd)):
            new_samples.append(even.pop())
            new_samples.append(odd.pop())
        even = even[::-1]
        new_samples.extend(even)
    return new_samples

print(even_and_odd([7, 3, 14, 17]))
print(even_and_odd([1, 3, 5, 7, 9, 11]))
print(even_and_odd([1, 2, 2, 4, 4, 6, 6, 2004, 9, 11]))