import pandas as pd

# file = pd.read_csv('utf_doro.csv')
# data = file.loc[file['si_do']=='대전광역시',['road_code','road_name','serial_number','si_do']]
# data.to_csv('daejeon.csv',mode='w')

file = pd.read_csv('medical.csv')
data = file.loc[file['si_do']=='대전',['num', 'si_do','si_gun_gu','name','address','phone']]
data.to_csv('medical_dj.csv',mode='w',sep='|')