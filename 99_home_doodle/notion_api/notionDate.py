from notion.client import NotionClient
from notion.block import TodoBlock, TextBlock
from notion.block import PageBlock

from decouple import config
from datetime import date, timedelta
from pprint import pprint

token = config('notion_token')
notion_url = config('notion_url')

client = NotionClient(token_v2=token)
page = client.get_block(notion_url)

info = dict()
start = date(year=2021, month=2, day=4)
d = timedelta(days=1)
cnt = 1
title_list = []
today = date.today()
print(today)
for i in range(300):
    if today>=start:
        start += d
        cnt *= -1
        continue
    title = start.strftime('%y-%m-%d')

    title_list.append(title)
    x = -1
    if not i%3:
        x = 1
    info[title]={
        'no':cnt, #샴푸 : 노비프록스
        'jin':-cnt, # 샴푸 : 진크피
        0:x, ## 저녁. '3일 저녁 : 제로큐탄'
        1:-cnt # '2일 : 아보다트'
    }
    start += d
    cnt *= -1

for title in title_list:
    print(title+' make')
    day_page = page.children.add_new(PageBlock)
    day_page.title = title
    print('page done')
    l = ['아침','점심','저녁']
    text = ''
    for i in range(3):
        text += l[i]
        if i==2:
            for j in range(2):
                if info[title][j]==1:
                    if j:
                        text += ' + 아보다트'
                    else:
                        text += ' + 제로큐탄'
        elif i == 0:
            if info[title]['no'] == 1:
                text += ' + 샴푸:노비프록스'
            else:
                text += ' + 샴푸:진크피'
            text+='\n\n'
        else:
            text+='\n\n'
    print('text make')
    todo = day_page.children.add_new(TextBlock)
    todo.title = text
