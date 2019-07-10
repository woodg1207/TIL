# 변수에 만들고 싶은 파일을 open()해야 한다. 
# f = open('만들파일명', '행동') r:읽기 w:쓰기 (덮어씌워짐) a: 추가
f = open('ssafy.txt','w')
#1~10
for i in range(10):
    f.write(f'this is line{i+1}.\n')#  \n : next line
f.close() #열었으면 닫아줘 ## 닫는걸 귀찮아서 with구문이 생김 (context manager)

with open('with_ssafy.txt','w') as f:
    for i in range(10):
        f.write(f'this is line{i+1}.\n')

#writelines() : 리스트를 넣어 주면, 요소 하나당 한 줄씩 작성한다. 
with open('ssafy.txt','w') as f:
    f.writelines(['0\n', '1\n', '2n\n', '3\n'])
