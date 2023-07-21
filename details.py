import os
import csv
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd
import re


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


res = requests.post(url, data=payload, headers=headers)
dfs = pd.read_html(res.text, header=None)
all_data = pd.concat(dfs)
current_dir = os.getcwd()
csv_path = os.path.join(current_dir, '詳細資料.csv')
all_data.to_csv(csv_path, index=False)


# 練習方法三:取得all_data，row的內容
index_of_description_row1 = 0 # 6414 樺漢在row 1 (index 0)
index_of_description_row6 = 5 # "說明" 在row 6 (index 5)

# Get the content of "說明" column from the first row
description_content_row1 = all_data.iloc[index_of_description_row1, 0]
description_content_row6 = all_data.iloc[index_of_description_row6, 5]


# 6414、樺漢
match_result = re.match(r'.*?(\d+)\s+([\u4e00-\u9fa5]+)\s+公司.*', description_content_row1)

if match_result:
    company_code = match_result.group(1)
    company_name = match_result.group(2)
else:
    print("not matched result")


# 說明的內容
# 分行
split_description = re.split(r'\s(?=\d+\.)', description_content_row6)

description_dict = {}
for item in split_description:
    num, content = re.match(r'(\d+)\.(.*)', item).groups()
    description_dict[int(num)] = content.strip()

#第五次 無擔保
match_result = re.search(r'國內(.*?)轉換公司債', description_dict[2])

if match_result:
    extracted_string = match_result.group(1).strip()
    splitted_result = extracted_string.split("次", 1)

    if len(splitted_result) == 2:
      part1 = splitted_result[0].strip()+"次"
      part2 = splitted_result[1].strip()
    else:
      print("split failed")
else:
    print("not matched result")

#發行總額
keyword = "總面額"
start_index = description_dict[4].find(keyword)

if start_index != -1:
    total_amount = description_dict[4][start_index + len(keyword):].strip()

else:
    print("keyword not matched")

print(f'1.股票代號: {company_code}\n'
      f'2.股票名稱: {company_name}\n'
      f'3.上市/上櫃: {part1}{part2}\n'
      f'4.決議日期:  {description_dict[1]}\n'
      f'5.發行總額:  {total_amount}\n'
      f'6.發行價格:  {description_dict[6]}\n'
      f'7.發行期間:  {description_dict[7]}\n'
      f'8.擔保品:  {description_dict[9]}\n'
      f'9.發行用途:  {description_dict[10]}\n'
      f'10.承銷方式:  {description_dict[11]}\n'
      f'11.受託人:  {description_dict[12]}\n'
      f'12.承銷:  {description_dict[13]}\n'
      f'13.轉換基準日:  {description_dict[20]}')

