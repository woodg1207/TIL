from collections import deque

def solution(begin, target, words):
    answer = 0
    w_dict = {}
    q = deque()
    for i in words:
        w_dict[i] = False
    for i in range(len(begin)):
        
    
    return w_dict






B = 'hit'
T = 'cog'
W = ['hot', 'dot', 'dog', 'lot', 'log', 'cog']	
print(solution(B,T,W))