import requests
from bs4 import BeautifulSoup
url = 'https://www.naver.com/'
html = requests.get(url).text
soup = BeautifulSoup(html, 'html.parser')
# rank = range(1,21)
# for sites in rank:
#     sites = 
sites = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
print(sites)
#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul:nth-child(6) > li:nth-child(1) > a.ah_a > span.ah_k
for site in sites:
    print(site.text)

#두번째 커밋을 위한 주석!!!