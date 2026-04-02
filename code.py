import requests
import json
import csv

# 設定連接的api
url = 'https://api.thecatapi.com/v1/images/search'

# 透過api用GET抓取資料
response = requests.get(url)

# 判斷是否GET成功，status_code == 200表示成功
if response.status_code == 200:
    cat_data = response.json()  # 儲存GET到的資料，將伺服器回傳的json資料轉成list

    # 回傳的資料儲存為json檔案
    with open('cats_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(cat_data, json_file, ensure_ascii=False, indent=4)
# 如果GET失敗
else:
    print(f"failed：{response.status_code}") # 輸出錯誤代碼
