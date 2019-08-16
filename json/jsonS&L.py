
import json

filename="username.json"

try:
     # 在try中放json.load()是因為如果username.json檔已經存在的話，就直接將名字載入記憶體中
     with open(filename) as file: 
        username=json.load(file)
except FileNotFoundError:
     # 如果檔案找不到時我們會提供使用者輸入訊息並寫入檔案中以便再開啟時可以紀錄原先輸入的名字
        username=input("What's your name ?")
        with open(filename,"w") as file:
                json.dump(username,file)        ''' json.dump() ==> json格式
                                                    由json.load()轉str儲存'''
        with open(filename) as rfile:     
                username=json.load(rfile)

        print("We'll remember you when you come back,"+username)
else:
    print("Welcome back,"+username)















