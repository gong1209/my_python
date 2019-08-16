import json 

filename="number.json" # 這行我們要確定是不是跟前面的讀取檔案名稱相同
with open(filename) as file: # 以讀取模式開啟檔案(若沒有第二個參數都是預設成讀取模式)
    numbers=json.load(file) # 用json.load()載入放在number.json檔裡面的資料，然後將它存到numbers變數中

print(numbers)













