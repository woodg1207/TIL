from notion.client import NotionClient
from notion.block import TodoBlock
from notion.block import PageBlock

from decouple import config
from datetime import date, timedelta
from pprint import pprint

token = config('notion_token')
notion_url = config('notion_url')

client = NotionClient(token_v2=token)
page = client.get_block(notion_url)


def notion(title, info):
    print(title)
    day_page = page.children.add_new(PageBlock)
    day_page.title = title
    for i in ['아침','점심','저녁']:
        todo = day_page.children.add_new(TodoBlock)
        todo.title = i
        todo.checked = False

    for key, value in info.items():
        if value == 1:
            todo = day_page.children.add_new(TodoBlock)
            todo.title = key
            todo.checked = False
    

info = dict()
start = date(year=2021, month=2, day=4)
d = timedelta(days=1)
cnt = 1
title_list = []
today = date.today()
print(today)
for i in range(5):
    if today>start:
        start += d
        cnt *= -1
        continue
    title = start.strftime('%y-%m-%d')

    title_list.append(title)
    x = -1
    if not i%3:
        x = 1
    info[title]={
        'shampooA':cnt,
        'shampooB':-cnt,
        'threedays':x,
        'pill':-cnt
    }
    start += d
    cnt *= -1
pprint(info)
print(title_list)
for title in title_list:
    break
    notion(title, info[title])