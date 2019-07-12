#텔레그램 요청
import requests
from decouple import config

api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
text = '안녕하세요'

send_message = requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')

print(send_message.text) ##json형식으로 터미널에 뜬다. 
