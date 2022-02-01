from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
import pandas as pd

A=0
while A==0:
    A+=1
    Count=0
    if Count==0:

        URL_1='https://coinmarketcap.com/new/'
        webpage1 = requests.get(URL_1)
        soup1 = BeautifulSoup(webpage1.content, "html.parser")
        Coin_MarkerCap = etree.HTML(str(soup1))

        Temp_List_1=[]

        for i in range(0, 5):
            Temp_List_1.append((Coin_MarkerCap.xpath('//*[@id="__next"]//tbody/tr['+str(i+1)+']/td[3]/a[1]/div[1]/div[1]/p')[0].text).replace('\n',''))
            print(Temp_List_1[i])
            url1 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(Temp_List_1[i])
            # requests.get(url1)
            # sleep(1)

        pd.DataFrame(Temp_List_1).to_csv('Tempp.csv')
