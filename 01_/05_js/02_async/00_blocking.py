from time import sleep

def sleep_3s():
    sleep(3)
    print('wake up!')

print('start sleeping')
sleep_3s()  # 수행되기 전까지 다음 줄이 진행이 안된다. blocking
print('end of program')