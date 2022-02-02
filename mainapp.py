from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
import pandas as pd
# import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("D:/Projects/sufyanpython-1f042e1fc067.json",scope)
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
    try:
        Count=0
        if Count==0:

            URL_1='https://coinmarketcap.com/new/'
            webpage1 = requests.get(URL_1)#, headers=HEADERS)
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
            
                    #print(main_list_1[i])
                    pass
                    # proxy = Random_Proxy()
                    
                    # url1 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(main_list_1[i])
                    # #url2 = 'https://api.telegram.org/bot5239619966:AAGoZ1maO870KNAbgt9olsC53eVNF0gv_AU/sendMessage?chat_id=256007064&parse_mode=MarkdownV2&&text=New Coin Arrived at Coin Gecko\n'+str(main_list[i])
                    # request_type = "get"

                    # #r = proxy.Proxy_Request(url=url2, request_type=request_type)
                    # r = proxy.Proxy_Request(url=url1, request_type=request_type)


            
        Count+=1
        sleep(5)
        
        if Count==1:
            
            URL_2 = "https://www.coingecko.com/en/coins/recently_added"
            webpage2 = requests.get(URL_2)#, headers=HEADERS)
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
                    pass
                    #print(main_list[i])
                    # proxy = Random_Proxy()
                    
                    # url2 = 'https://api.telegram.org/bot5179356592:AAFJQqOMJkMocIH0SU5J4GnmfhK6EE-_tno/sendMessage?chat_id=5050252731&parse_mode=MarkdownV2&&text=Program 2 New Coin Arrived at Coin Gecko\n'+str(main_list[i])
                    # #url2 = 'https://api.telegram.org/bot5239619966:AAGoZ1maO870KNAbgt9olsC53eVNF0gv_AU/sendMessage?chat_id=256007064&parse_mode=MarkdownV2&&text=New Coin Arrived at Coin Gecko\n'+str(main_list[i])
                    # request_type = "get"

                    # #r = proxy.Proxy_Request(url=url2, request_type=request_type)
                    # r = proxy.Proxy_Request(url=url2, request_type=request_type)
                    # sleep(2)


            sheet_3 = client.open("@BorisJohnson")
            sheet_instance_3 = sheet_3.get_worksheet(2)
            a_3=sheet_instance_3.get_all_records()
            records_df_3 = pd.DataFrame.from_dict(a_3)
            # print(records_df_3)
            Loaded_List_3=list(records_df_3['list'])
            # print(Loaded_List_3)
            sheet_instance_3.update_acell('A'+str(len(Loaded_List_3)+2),'Refreshed')
           
        
    except:
        
        pass
