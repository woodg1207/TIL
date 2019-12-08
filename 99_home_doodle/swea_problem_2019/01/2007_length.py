import sys
sys.stdin = open('t2007.txt', 'r')

testcase = int(input())
for sample in range(testcase):
    words = input()
    box = words[:10]
    # for i in words:

    print(box)