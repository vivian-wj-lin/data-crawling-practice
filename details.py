from bs4 import BeautifulSoup
import requests
import json
import pandas as pd


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

url = "https://mops.twse.com.tw/mops/web/ajax_t05st01"
payload = {
  "step": "2",
  "colorchg": "1",
  "co_id": "6414",
  "TYPEK": "sii",
  "off": "1",
  "firstin": "1",
  "i": "22",
  "year": "2023",
  "month": "0",
  "spoke_date": "20230706",
  "spoke_time": "145811",
  "seq_no": "5",
  "b_date": "1",
  "e_date": "1",
  "t51sb10": "t51sb10"
}


res = requests.post(url, data=payload, headers=headers).text
print(res)

soup = BeautifulSoup(res, "html.parser")
df_list = pd.read_html(str(soup))
print(df_list) # No tables found


