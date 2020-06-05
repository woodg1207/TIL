import time

t = time.localtime()
# print(t)
t1 = time.strftime('%Y-%m-%d %X', t)
print(t1)