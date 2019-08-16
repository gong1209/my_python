import json

numbers=[1,2,3,4,5,6] 

filename="number.json" # 指定要把numbers串列存到number.json檔中
with open(filename,"w") as file: # 以寫入模式開啟檔案才可以將資料儲存進去
    json.dump(numbers,file) # 將numbers串列存到number.json檔





