"""
DOCstring >> 가이드라인 함수 설명 할 때 사용 주석용도와 다르다. 
"""

with open('quest.txt','w') as f:
    for i in range(4):
        f.write(f'{i}\n')

with open('quest.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        print(line.strip())
        
with open('reverse_quest.txt', 'w') as f:
    lines.reverse()
    for r_line in lines:
        f.write(f'{r_line}')
