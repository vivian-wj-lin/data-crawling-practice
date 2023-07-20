from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# df = pd.read_csv('112年上市公司轉換公司債.csv')

# filtered_data = df[df['代號'] == '6414']

# print(filtered_data)
#      代號  簡稱         日期 序號                       主旨  Unnamed: 5
# 1   6414  樺漢  112/07/17  4      公告本公司各次轉換公司債之轉換價格調整         NaN
# 24  6414  樺漢  112/07/06  5  董事會決議發行本公司國內第五次無擔保轉換公司債         NaN

headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}

url = "https://mops.twse.com.tw/mops/web/ajax_t05st01"
payload = {
  "seq_no": "5",
  "spoke_time": "145811",
  "spoke_date": "20230706",
  "i": "22",
  "co_id": "6414",
  "TYPEK": "sii"
}

# res = requests.post(url, data=payload, headers=headers).text
# print(res)

## soup = BeautifulSoup(res2, "html.parser")
## df_list = pd.read_html(str(soup))
## print(df_list) # No tables found


# mops2.js

# https://mops.twse.com.tw/mops/web/ajax_t05st01

# {
#   "step": "2",
#   "colorchg": "1",
#   "co_id": "6414",
#   "TYPEK": "sii",
#   "off": "1",
#   "firstin": "1",
#   "i": "22",
#   "year": "2023",
#   "month": "0",
#   "spoke_date": "20230706",
# "spoke_time": "145811",
#   "seq_no": "5",
#   "b_date": "1",
#   "e_date": "1",
#   "t51sb10": "t51sb10"}
	#status=200, <title>公開資訊觀測站</title>

# https://mops.twse.com.tw/mops/web/ajax_t05st01
# {"h260":"樺漢",
# "h261":"6414",
# "h262":"20230706",
# "h264":"董事會決議發行本公司國內第五次無擔保轉換公司債",
# "h263":"145811",
# "h265":"5",
# "h266":"sii",
# "h267":"22",
# "h268":"20230706",
# "h269":"2",
# "t51sb10":"t51sb10"
# }
	#status=200, <title>公開資訊觀測站</title>
