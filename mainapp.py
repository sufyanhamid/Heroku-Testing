from bs4 import BeautifulSoup
from lxml import etree
import requests
from time import sleep
import pandas as pd
# import random
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint as pp
import random




scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',"https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name("sufyanpython-1f042e1fc067.json",scope)
client = gspread.authorize(creds)

while True:
    sheet_3 = client.open("@BorisJohnson")
    sheet_instance_3 = sheet_3.get_worksheet(2)
    a_3=sheet_instance_3.get_all_records()
    records_df_3 = pd.DataFrame.from_dict(a_3)
    # print(records_df_3)
    Loaded_List_3=list(records_df_3['list'])
    # print(Loaded_List_3)
    sheet_instance_3.update_acell('A'+str(len(Loaded_List_3)+2),'Refreshed')
    sleep(5)
