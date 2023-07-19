from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# 讀取 CSV 檔案
df = pd.read_csv('112年上市公司轉換公司債.csv')

# 篩選代號為 6414 的資料
filtered_data = df[df['代號'] == '6414']

# 印出篩選後的資料
print(filtered_data)
