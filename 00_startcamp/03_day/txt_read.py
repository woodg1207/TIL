#read() : 개행문자를 포함한 하나의 문자열
with open('with_ssafy.txt', 'r') as f:
    all_text = f.read()
    print(all_text)


# readlines() :  파일의 모든 라인을 읽어서 각각의 줄을 요소로 갖는 list로 만들어냄
with open('with_ssafy.txt', 'r') as f:
    lines = f.readlines()#list 변수
    for line in lines:
        print(line.strip())
        #print함수내에도 개행문자가 있고 lines 리스트(파일내) 개행이 있어 중복 
        # => .strip()을 통해 list내의 개행문자 삭제
        # dir()을 통해 함수를 찾기 가능 => print(dir())
        #print(dir(line))
