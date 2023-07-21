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


# all_data = all_data.astype(str)
# all_data[1] = all_data[1].astype(str)
# # print(all_data)
# # print(type(all_data)) #DataFrame
# # print(type(all_data[1])) #Series


# 練習方法一: all_data[1]，series
# # 將 all_data[1] 中的每個元素轉換為字符串

# # 董事會決議日期
# resolutions_date_match = all_data[1].str.extract(r'(董事會決議日期:\d{3}/\d{2}/\d{2})', expand=False)
# # print(resolutions_date_match) #成功
# # print(type(resolutions_date_match)) #Series

# filtered_series = resolutions_date_match.dropna()# 過濾出非NaN的值
# date_str = filtered_series.iloc[0] if not filtered_series.empty else None

# print(date_str)


# 練習方法二: all_data，Dataframe
# all_data = pd.DataFrame([
#     ["本資料由　(上市公司) 6414 樺漢 公司提供"],
#     ["序號"],
#     ["發言日期"],
#     ["發言人"],
#     ["發言人職稱"],
#     ["發言人電話"],
#     ["主旨"],
#     ["符合條款"],
#     ["事實發生日"],
#     ["說明"]
# ], columns=[1])


# pattern_str = r"本資料由　\(上市公司\) (\d+) (.+?) 公司提供"
# pattern = re.compile(pattern_str)

# # 抓第 1 行文字
# data_text = all_data.loc[0, 1]

# match = pattern.search(data_text)

# if match:
#     company_code = match.group(1)
#     company_name = match.group(2)
# else:
#     company_code = None
#     company_name = None

# print("公司代碼:", company_code)
# # print(type(company_code))#str
# print("公司名稱:", company_name)
# # print(type(company_name))#str


# 練習方法三:取得all_data，row的內容
index_of_description_row1 = 0 # 6414 樺漢在row 1 (index 0)
index_of_description_row6 = 5 # "說明" 在row 6 (index 5)

# Get the content of "說明" column from the first row
description_content_row1 = all_data.iloc[index_of_description_row1, 0]
description_content_row6 = all_data.iloc[index_of_description_row6, 5]

# print(description_content_row1)
# print(description_content_row6)



# 6414、樺漢
match_result = re.match(r'.*?(\d+)\s+([\u4e00-\u9fa5]+)\s+公司.*', description_content_row1)

if match_result:
    company_code = match_result.group(1)
    company_name = match_result.group(2)
    print(company_code)
    print(company_name)
else:
    print("not matched result")


# 說明的內容
# 分行
split_description = re.split(r'\s(?=\d+\.)', description_content_row6)

description_dict = {}
for item in split_description:
    num, content = re.match(r'(\d+)\.(.*)', item).groups()
    description_dict[int(num)] = content.strip()

# print(description_dict)

# print(description_dict[1])

# print(description_dict[2])
match_result = re.search(r'國內(.*?)轉換公司債', description_dict[2])

if match_result:
    extracted_string = match_result.group(1).strip()
    print(extracted_string)
    splitted_result = extracted_string.split("次", 1)

    if len(splitted_result) == 2:
      part1 = splitted_result[0].strip()+"次"
      part2 = splitted_result[1].strip()
      print(part1)
      print(part2)
    else:
      print("split failed")
else:
    print("not matched result")


# print(description_dict[4])

keyword = "總面額"
start_index = description_dict[4].find(keyword)

if start_index != -1:
    extracted_string = description_dict[4][start_index + len(keyword):].strip()
    print(extracted_string)
else:
    print("keyword not matched")

# print(description_dict[6])
# print(description_dict[7])
# print(description_dict[9])
# print(description_dict[10])
# print(description_dict[11])
# print(description_dict[12])
# print(description_dict[20])
    