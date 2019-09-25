import sys
sys.stdin = open('seven.txt', 'r')

arr=[[i for i in input()] for _ in range(5)]
print(arr)