import os
from bs4 import BeautifulSoup
import requests
import pandas as pd

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

url = 'https://mops.twse.com.tw/mops/web/ajax_t51sb10'

payload = {
    "encodeURIComponent": 1,
    "step": 1,
    "firstin": True,
    "id": "",
    "key": "",
    "TYPEK": "",
    "Stp": 4,
    "go": False,
    "co_id": "",
    "r1": 1,
    "KIND": "L",
    "CODE": "",
    "keyWord": "轉換公司債",
    "Condition2": 1,
    "keyWord2": "",
    "year": 112,
    "month1": 0,
    "begin_day": 1,
    "end_day": 1,
    "Orderby": 1
}

res = requests.post(url, data=payload, headers=headers).text

dfs = pd.read_html(res)

df = dfs[0]

current_dir = os.getcwd()

csv_path = os.path.join(current_dir, '112年上市公司轉換公司債.csv')

df.to_csv(csv_path, index=False)

