from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
import pandas as pd
# import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp

scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sufyanpython-1f042e1fc067.json",scope)
client = gspread.authorize(creds)



def My_Sheet(sheet_number, latest_data):
    sheet = client.open("@BorisJohnson")
    sheet_instance = sheet.get_worksheet(sheet_number)
    for i in range(0,len(latest_data)):
        sheet_instance.update_acell('A'+str(i+2),latest_data[i])

HEADERS = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 \
            (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',\
            'Accept-Language': 'en-US, en;q=0.5'})


while True:
    
    Count=0
    if Count==0:

        URL_1='https://coinmarketcap.com/new/'
        webpage1 = requests.get(URL_1, headers=HEADERS)
        soup1 = BeautifulSoup(webpage1.content, "html.parser")
        Coin_MarkerCap = etree.HTML(str(soup1))

        Temp_List_1=[]
        main_list_1=[]
        
        for i in range(0, 10):
            Temp_List_1.append((Coin_MarkerCap.xpath('//*[@id="__next"]//tbody/tr['+str(i+1)+']/td[3]/a[1]/div[1]/div[1]/p')[0].text).replace('\n',''))

        sheet_1 = client.open("@BorisJohnson")
        sheet_instance_1 = sheet_1.get_worksheet(0)
        b=sheet_instance_1.get_all_records()        
        records_df_1 = pd.DataFrame.from_dict(b)
        Loaded_List_1=list(records_df_1['Coins'])
        #File_1=pd.read_csv('./Desktop/New_List_1.csv',index_col=False)
        main_list_1 = list(set(Temp_List_1) - set(Loaded_List_1))

        if main_list_1:
            My_Sheet(0,Temp_List_1)
#             Temp_File_1=pd.DataFrame(Temp_List_1).to_csv('./Desktop/New_List_1.csv',index=False)
            for i in range(0, len(main_list_1)):
                url1 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(main_list_1[i])
                requests.get(url1)
                sleep(2)

        
    Count+=1
    sleep(50)
    
    if Count==1:
        
        URL_2 = "https://www.coingecko.com/en/coins/recently_added"
        webpage2 = requests.get(URL_2, headers=HEADERS)
        soup2 = BeautifulSoup(webpage2.content, "html.parser")
        Coin_Gecko = etree.HTML(str(soup2))
        
        sleep(2)

        Temp_List=[]
        main_list=[]
        
        for i in range(0, 10):
            Temp_List.append((Coin_Gecko.xpath('/html/body/div[2]/div[5]/div[3]/div[2]/div/table/tbody/tr['+str(i+1)+']/td[3]/div/div[2]/div/a[1]')[0].text).replace('\n',''))    
        
        sheet = client.open("@BorisJohnson")
        sheet_instance = sheet.get_worksheet(1)
        a=sheet_instance.get_all_records()        
        records_df = pd.DataFrame.from_dict(a)
        Loaded_List=list(records_df['Coins'])

        main_list = list(set(Temp_List) - set(Loaded_List))

        if main_list:
            My_Sheet(1,Temp_List)
            for i in range(0, len(main_list)):
                url1 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(main_list[i])
                requests.get(url1)
                sleep(2)

                #         sleep(28)














# class Random_Proxy(object):

#     def __init__(self):
#         self.__url = 'https://www.sslproxies.org/'
#         self.__headers = {
#             'Accept-Encoding': 'gzip, deflate, sdch',
#             'Accept-Language': 'en-US,en;q=0.8',
#             'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36',
#             'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
#             'Referer': 'http://www.wikipedia.org/',
#             'Connection': 'keep-alive',
#             }
#         self.random_ip = []
#         self.random_port = []

#     def __random_proxy(self):

#         """
#         This is Private Function Client Should not have accesss
#         :return: Dictionary object of Random proxy and port number
#         """

#         r = requests.get(url=self.__url, headers=self.__headers)
#         soup = BeautifulSoup(r.text, 'html.parser')

#         # Get the Random IP Address
#         for x in soup.findAll('td')[::8]:
#             self.random_ip.append(x.get_text())

#         # Get Their Port
#         for y in soup.findAll('td')[1::8]:
#             self.random_port.append(y.get_text())

#         # Zip together
#         z = list(zip(self.random_ip, self.random_port))

#         # This will Fetch Random IP Address and corresponding PORT Number
#         number = random.randint(0, len(z)-50)
#         ip_random = z[number]

#         # convert Tuple into String and formart IP and PORT Address
#         ip_random_string = "{}:{}".format(ip_random[0],ip_random[1])

#         # Create a Proxy
#         proxy = {'https':ip_random_string}

#         # return Proxy
#         return proxy

#     def Proxy_Request(self,request_type='get',url='',**kwargs):
#         """

#         :param request_type: GET, POST, PUT
#         :param url: URL from which you want to do webscrapping
#         :param kwargs: any other parameter you pass
#         :return: Return Response
#         """
#         while True:
#             try:
#                 proxy = self.__random_proxy()
# #                 print("Using Proxy {}".format(proxy))
#                 r = requests.request(request_type,url,proxies=proxy,headers=self.__headers ,timeout=8, **kwargs)
#                 return r
#                 break
#             except:
#                 pass
            

# A=0
# while A==0:
#     A+=1
#     Count=0
#     if Count==0:

#         URL_1='https://coinmarketcap.com/new/'
#         webpage1 = requests.get(URL_1)
#         soup1 = BeautifulSoup(webpage1.content, "html.parser")
#         Coin_MarkerCap = etree.HTML(str(soup1))

#         Temp_List_1=[]

#         for i in range(0, 5):
#             Temp_List_1.append((Coin_MarkerCap.xpath('//*[@id="__next"]//tbody/tr['+str(i+1)+']/td[3]/a[1]/div[1]/div[1]/p')[0].text).replace('\n',''))
#             print(Temp_List_1[i])
#             url1 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(Temp_List_1[i])
            
#             request_type = "get"
#             proxy = Random_Proxy()
#             proxy.Proxy_Request(url=url1, request_type=request_type)

#         # pd.DataFrame(Temp_List_1).to_csv('Tempp.csv')
