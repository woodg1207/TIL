import os
#1. 해당 파일들이 있는 위치로 이동
os.chdir(r'C:\Users\student\Desktop\TIL\00_startcamp\02_day\change_filenames')#   \때문에  r을 주소 앞에 써준다. 
#2. 현재 폴더 안에 모든 파일 이름을 수집
filenames = os.listdir('.')  # os.listdir('디렉토리 주소')  .은 현재위치를 의미한다.  #  파일 리스트를 구했음
#3.각각의 파일명을 돌면서 수정한다. 
#os.rename(현재이름, 바꿀이름)이름 재설정
# for filename in filenames:
#      os.rename(filename,f'SAMSUNG_{filename}')

# samsung 을  ssafy로 변환 
for filename in filenames:
     os.rename(filename, filename.replace('SAMSUNG_', 'SSAFY_'))       # 'happy.replace('h','b') h를 b로바꿈
