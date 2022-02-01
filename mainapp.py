from bs4 import BeautifulSoup
from lxml import etree
import requests

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})

URL_2 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 3 New Coin Arrived at Coin Gecko'

requests.get(URL_2)#, headers=HEADERS)
print(URL_2)
